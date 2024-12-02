class MM1SJFQueueSimulation:
    def __init__(self, env, lambd, mu):
        self.env = env
        self.lambd = lambd
        self.mu = mu
        self.waiting_times = []
        self.queue = []
        self.server_busy = False

    def arrival_process(self):
        '''
        Generator function to simulate the arrival process of customers in thw queue system.
        '''
        while True:
            # Calculate time until next arrival
            yield self.env.timeout(random.expovariate(1/self.lambd))

            # Calculate service and arrival times to sort shortest job
            arrival_time = self.env.now
            service_time = random.expovariate(1/self.mu)

            # Stores and sorts jobs based on service time into queue
            self.queue.append((arrival_time, service_time))
            self.queue.sort(key=lambda x: x[1])

            # If server is free, continue to the service process
            if not self.server_busy:
                self.env.process(self.service_process())

    def service_process(self):
        '''
        Generator function to simulate the service process for jobs in the queue.
        '''
        while self.queue:
            # Completes service process and removes shortest job from queue when done
            self.server_busy = True
            arrival_time, service_time = self.queue.pop(0)# Shortest job in the queue is always served first
            waiting_time = self.env.now - arrival_time
            self.waiting_times.append(waiting_time)

            yield self.env.timeout(service_time)

        self.server_busy = False #Set the server status to free when there are no jobs left

    def average_wait_time_run(self, simulation_time):
        '''
        Generator function to calculate the wait times for
        '''
        self.env.process(self.arrival_process())
        self.env.run(until=simulation_time)
        avg_waiting_time = np.mean(self.waiting_times) if self.waiting_times else 0

        return avg_waiting_time
