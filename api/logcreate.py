from time import sleep
import logging

# Define the logger details
logging.basicConfig(filename="logFile.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


if __name__=="__main__":
    cycle = 0
    while(True):
        logging.error(f'python-logstash: test logstash error message.: {cycle}')
        logging.info(f'python-logstash: test logstash info message.: {cycle}')
        logging.warning(f'python-logstash: test logstash warning message.: {cycle}')
        logging.info(f'python-logstash: test extra fields: {cycle}')
        print(f'Cycle Complete : {cycle}')
        cycle+=1
        sleep(5)