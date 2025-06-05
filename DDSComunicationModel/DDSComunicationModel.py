import traceback,time
import sys,os
sys.path.append('.')
from Base.BaseNode import BaseNode
from Base import BaseNodeData

from IDL.dds import linParserData
from IDL.dds import SomeIpParserData
from IDL.dds import canMessageData
from fastdds_adapter import fastdds


class ReaderListener(fastdds.DataReaderListener):
    def __init__(self,reader,dataType,callbackFunc):
        self.reader = reader
        self.data_type = dataType
        self.call_back_func = callbackFunc
        super().__init__()

    def on_data_available(self, reader):
        try:
            info = fastdds.SampleInfo()
            try:
                if self.data_type is linParserData.linFrames :
                    data = linParserData.linFrames() 
                elif self.data_type is SomeIpParserData.frame :
                    data = SomeIpParserData.frame() 
                elif self.data_type is canMessageData.canMessage :
                    data = canMessageData.canMessage()
            except Exception as e_ :
                print(e_)
            reader.take_next_sample(data, info)
            self.call_back_func(data)
        except Exception as e_ :
            print(traceback.format_exc())

    def on_subscription_matched(self, datareader, info) :
        if (0 < info.current_count_change) :
            print ("log replay Subscriber matched publisher {}".format(info.last_publication_handle))
        else :
            print ("log replay unmatched publisher {}".format(info.last_publication_handle))

def single_class(cls) :
    instance = {}
    def single(*args,**kargs) :
        if cls not in instance :
            instance[cls] = cls(*args,**kargs)
            return instance[cls]
        else :
            return instance[cls]
    return single

@single_class
class DDSComunication(BaseNode) :
    def __init__(self, name: str, DomainID: int = 0) -> None:
        super().__init__(name, DomainID)
        self._lin_recv = list()
        self._someip_package_recv = list()
        self._someip_calling_recv = list()
        self._can_uds_recv = list()
        self._fastdds_reader_init()

    def _fastdds_reader_init(self) :
        self.topic_qos = fastdds.TopicQos()
        self.participant.get_default_topic_qos(self.topic_qos)

        self.reader_qos = fastdds.DataReaderQos()
        self.reader_qos.reliability().kind = fastdds.BEST_EFFORT
        self.reader_qos.durability().kind = fastdds.VOLATILE_DURABILITY_QOS
        self.reader_qos.data_sharing().automatic()
        self.subscriber.set_default_datareader_qos(self.reader_qos)

        ###lin parser topic
        self.linParserData_topic_data_type =   linParserData.linFramesPubSubType() 
        self.linParserData_topic_data_type.setName(BaseNodeData.linParserTopic.IDL)
        self.linParserData_type_support = fastdds.TypeSupport(self.linParserData_topic_data_type)
        self.participant.register_type(self.linParserData_type_support)
        self.topic_lin_parser = self.participant.create_topic\
            (BaseNodeData.linParserTopic.NAME,self.linParserData_topic_data_type.getName(), self.topic_qos)
        self.listener_lin_parser = ReaderListener(self,linParserData.linFrames,self._lin_frame_callback)
        self.reader_lin = self.subscriber.create_datareader(self.topic_lin_parser, self.reader_qos, self.listener_lin_parser)

        ###someip package calling topic
        self.someIpParserData_topic_data_type =   SomeIpParserData.framePubSubType() 
        self.someIpParserData_topic_data_type.setName(BaseNodeData.someipPackage.IDL)
        self.someIpParserData_type_support = fastdds.TypeSupport(self.someIpParserData_topic_data_type)
        self.participant.register_type(self.someIpParserData_type_support)

        self.topic_someIp_package_parser = self.participant.create_topic\
            (BaseNodeData.someipPackage.NAME,self.someIpParserData_topic_data_type.getName(), self.topic_qos)
        self.listener_someIp_package_parser = ReaderListener(self,SomeIpParserData.frame,self._someip_package_callback)
        self.reader_someip_package = self.subscriber.create_datareader(self.topic_someIp_package_parser, self.reader_qos, self.listener_someIp_package_parser)

        self.topic_someIp_calling_parser = self.participant.create_topic\
            (BaseNodeData.someIpCalling.NAME,self.someIpParserData_topic_data_type.getName(), self.topic_qos)
        self.listener_someIp_calling_parser = ReaderListener(self,SomeIpParserData.frame,self._someip_calling_callback)
        self.reader_someip_calling = self.subscriber.create_datareader(self.topic_someIp_calling_parser, self.reader_qos, self.listener_someIp_calling_parser)
        
        # can uds topic
        self.canUdsMessageData_topic_data_type = canMessageData.canMessagePubSubType()
        self.canUdsMessageData_topic_data_type.setName(BaseNodeData.canUdsTopic.IDL)
        self.canUdsMessageData_type_support = fastdds.TypeSupport(self.canUdsMessageData_topic_data_type)
        self.participant.register_type(self.canUdsMessageData_type_support)
        self.topic_can_uds = self.participant.create_topic(BaseNodeData.canUdsTopic.NAME,self.canUdsMessageData_topic_data_type.getName(), self.topic_qos)
        self.listener_can_uds = ReaderListener(self, canMessageData.canMessage, self._can_uds_callback)
        self.reader_can_uds = self.subscriber.create_datareader(self.topic_can_uds, self.reader_qos, self.listener_can_uds)

    def _lin_frame_callback(self,frames:linParserData.linFrames) :
        for callback_func in self._lin_recv :
            callback_func(frames)

    def regsister_lin_recv(self,func) :
        if func not in self._lin_recv :
            self._lin_recv.append(func)
    
    def unregsister_lin_recv(self,func) :
        if func in self._lin_recv :
            self._lin_recv.remove(func)

    def _someip_package_callback(self,frame:SomeIpParserData.frame) :
        for callback_func in self._someip_package_recv :
            callback_func(frame)

    def regsister_someip_package_recv(self,func) :
        if func not in self._someip_package_recv :
            self._someip_package_recv.append(func)
    
    def unregsister_someip_package_recv(self,func) :
        if func in self._someip_package_recv :
            self._someip_package_recv.remove(func)

    def _someip_calling_callback(self,frame:SomeIpParserData.frame) :
        for callback_func in self._someip_calling_recv :
            callback_func(frame)
    
    def regsister_someip_calling_recv(self,func) :
        if func not in self._someip_calling_recv :
            self._someip_calling_recv.append(func)

    def unregsister_someip_calling_recv(self,func) :
        if func in self._someip_calling_recv :
            self._someip_calling_recv.remove(func)

    def _can_uds_callback(self, messages: canMessageData.canMessage):
        if self._can_uds_recv :
            for callback_func in self._can_uds_recv :
                callback_func(messages)

    def register_can_uds_recv(self,func) :
        if func not in self._can_uds_recv :
            self._can_uds_recv.append(func)

    def unregister_can_uds_recv(self, func):
        if func in self._can_uds_recv :
            self._can_uds_recv.remove(func)

        
