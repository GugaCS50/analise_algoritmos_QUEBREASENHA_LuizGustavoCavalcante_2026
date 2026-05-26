import random 
import string

class Oracle:

    def __init__(self, mode="random", path=None):

        self.charset = string.ascii_letters+string.digits
        self.oracle_hits = 0

        if mode == "file":

            with open(path, 'r') as f:
                self.secret_password = f.read().strip()

        else:

            self.secret_password = ''.join(
                random.choice(self.charset)
                for _ in range(8)
            )

#força bruta

    def check_full(self, attempt):

        self.oracle_hits += 1

        return attempt == self.secret_password
    
#divisão 

    def check_partial(self, part, start_pos):
        
        self.oracle_hits += 1
        end = start_pos + len(part)

        return(self.secret_password[start_pos:end]==part)
    
#genético

    def get_fitness(self, attempt):
        
        self.oracle_hits += 1
        score = 0

        for i in range(8):
            if attempt[i] == self.secret_password[i]:
                score += 1 

        return score
    
#resultado

    def get_hits(self):
        
        return self.oracle_hits