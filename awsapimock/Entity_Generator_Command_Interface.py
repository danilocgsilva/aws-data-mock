import abc

class Entity_Generator_Command_Interface(abc.ABC):

    @abc.abstractmethod
    def generate(self) -> dict:
        pass
