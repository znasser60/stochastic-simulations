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
