class ExClass:
    @staticmethod
    def ex_static_function(num):
        pass
        '''
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance!
        '''

    @classmethod
    def ex_class_function(cls):
        pass
        '''
        This should also do something that has a relationship
        with the class, but usualy, those are used to
        manipulate different structures of data to instantiate
        objects, like we have done with CSV.
        '''
