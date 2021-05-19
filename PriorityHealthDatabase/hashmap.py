class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(self.array_size)]

    def hash(self, key, collisions=0):
        key_bytes = str(key).encode()
        hash_code = sum(key_bytes)
        return hash_code + collisions 

    def compressor(self, hash_code):
        return hash_code % self.array_size 

    
    def setter(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value == None:
            self.array[array_index] = [key, value]
            return None 
        
        elif current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return None 
        
        number_collisions = 1
        while current_array_value[0] != key:
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            new_array_value = self.array[new_array_index]

            if new_array_value == None:
                self.array[new_array_index] = [key, value]
                return None 
            
            elif new_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return None 
            
            number_collisions += 1
        
    def getter(self, key):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value == None:
            return None 
        
        elif current_array_value[0] == key:
            return current_array_value[1]
        
        retrieve_collisions = 1
        while current_array_value[0] != key:
            new_hash_code = self.hash(key, retrieve_collisions)
            new_array_index = self.compressor(new_hash_code)
            new_array_value = self.array[new_array_index]

            if new_array_value == None:
                return None 

            elif new_array_value[0] == key:
                return current_array_value[1]
            
            retrieve_collisions += 1
            

    def delete(self, key):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value == None:
            pass
            return

        elif current_array_value[0] == key:
            self.array[array_index] =  None 
            return 

        del_collisions = 1

        while current_array_value[0] != key:
            new_hash_code = self.hash(key, del_collisions)
            new_array_index = self.compressor(new_hash_code)
            new_array_value = self.array[new_array_index]

            if new_array_value == None:
                pass

            elif new_array_value[0] == key:
                self.array[new_array_index] = None 
                return 

            del_collisions += 1