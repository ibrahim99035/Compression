class ArthClass:

    def __init__(self, frequency_table):
        self.probability_table = self.get_probability_table(frequency_table)
        

    def get_probability_table(self, frequency_table):
        total_frequency = sum(list(frequency_table.values()))

        probability_table = {}
        for key, value in frequency_table.items():
            probability_table[key] = value/total_frequency

        return probability_table
    
    
    def process_stage(self, probability_table, stage_min, stage_max):
        stage_probs = {}
        stage_domain = stage_max - stage_min
        for term_idx in range(len(probability_table.items())):
            term = list(probability_table.keys())[term_idx]
            term_prob = probability_table[term]
            cum_prob = stage_min + term_prob * stage_domain 
            stage_probs[term] = [stage_min, cum_prob]
            stage_min = cum_prob
        return stage_probs

    def get_encoded_value(self, encoder):

        last_stage = list(encoder[-1].values())
        last_stage_values = []
        
        for sublist in last_stage:
            for element in sublist:
                last_stage_values.append(element)
        last_stage_min = min(last_stage_values)
        last_stage_max = max(last_stage_values)

        return (last_stage_min + last_stage_max)/2



    def encode(self, msg, probability_table):  

        encoder = []
    
        stage_min = 0.0
        stage_max = 1.0

        for msg_term_idx in range(len(msg)):
            stage_probs = self.process_stage(probability_table, stage_min, stage_max)
            msg_term = msg[msg_term_idx]
            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]
            encoder.append(stage_probs)
       
        stage_probs = self.process_stage(probability_table, stage_min, stage_max)
        encoder.append(stage_probs)
        encoded_msg = self.get_encoded_value(encoder)
        
        return encoder, encoded_msg