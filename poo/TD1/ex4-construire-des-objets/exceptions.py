class ContainerError(Exception):
    pass


class ArrayError(ContainerError):
    pass


class StackError(ContainerError):
    pass


class QueueError(ContainerError):
    pass
