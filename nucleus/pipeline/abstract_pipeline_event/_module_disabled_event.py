from ._abstract_pipeline_event import AbstractPipelineEvent


class ModuleDisabledEvent(AbstractPipelineEvent):
    """A module was disabled

    module - the module that was disabled.
    """

    def __init__(self, module):
        """Constructor

        module - the module that was enabled
        """
        super(self.__class__, self).__init__(is_pipeline_modification=True)
        self.module = module

    def event_type(self):
        return "Module disabled"