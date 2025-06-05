// Version = 1.0.20220202
include "Common.thrift"
include "CanStackNode.thrift"



service canParserNode {

    Common.result setCrcRcConfig (1: pduCrcRcConfig req)
    Common.result clearAllCrcRcConfig ()
    Common.result clearCrcRcConfig (1: pduCrcRcConfig req)
    Common.result sendCanFrameCyc (1: CanStackNode.canMessage req)
    Common.result sendCanPduCyc (1: pduMessage req)
    Common.result sendCanPduCycList (1: pduMessages req)
    Common.result sendCanPdu (1: pduMessage req)

	// 添加一个CANDB文件
	Common.result addDbFile (1: dbPath req)
	// 配置通道和CANDB的关联
	Common.result setConfig (1: dbConfigs req)
	// 获取当前后台已经配置的 CanConfig_pair
	dbConfigs getCanDbConfigs ()

	// 获取当前已经加载的 can db config
	dbPath getCanDbPath ()

    Common.result subscribeMsg (1: subscribeInfo req)


    Common.result unSubscribeMsg (1: subscribeInfo req)
    //获取当前 Can的信息
    canDbInfo getCanDbInfo ()



	// 清除所有CANDB文件
	Common.result clear ()

	// 清除所有订阅
	Common.result clearSubscribe ()

	// 根据 PDU 的内容获取 PDU 的编码
	// i_signal_i_pdu_encode.result 错误原因
	// 0         获取编码成功
	// 1000      raise Error
	// 1         找不到对应的通道
	// 2         找不到对应的 PDU 名字
	// 3         找不到 PDU context 中指定的信号名
	iSignalIPduEncode encodePdu (1: iSignalIPduObj req)

	// 转换 CanDb 文件到 Py
	Common.result convertCanDbToPy (1: convertInput req)
	// 转换 CanDb 文件到 Json
	Common.result convertCanDbToJson (1: convertInput req)


}

struct pduCrcRcConfig {
	1: i32 channel // CAN 通道
	2: string pduName // PDU 的名字
	3: optional i32 crcBitStarts // CRC 的 byte
	5: optional i32 rcBitStarts // RC 的起始 bit
	7: optional list<i32> crcTable // CRC 的 table
	8: optional string crcName
	9: optional string rcName
	10: list<i32> rcConfig
}



struct pduMessage {
	1: i32 channel
	2: string pduName
	3: i32 period
    4: optional list<i32> data
    // YUE 为了验证可行性，快速适配之前的方案，实际上效率低且有BUG,待后续大更新
    5: string updateBy
    6: optional map<string,i32> context
    7: i32 times
    8: optional map<string,i32> context_raw
    9: list<list<i32>> padding_bit_list
}

struct pduMessages{
    1:list<pduMessage> message
}

struct subscribeInfo {
	1: i32 channel
	2: string name
	3: string type
}
struct dbPath {
	1: Common.result result
	2: string dbPath
}
struct dbConfigs {
	1: Common.result result
	2: list<dbConfigPair> configs
}
struct dbConfigPair {
	1: i32 channel
	2: string dbName
}

struct canDbInfo {
	1: Common.result result
	2: string strJson
}
struct iSignalIPduObj {
	1: i32 channel
	2: string pduName
	3: string pduContext
}
struct iSignalIPduEncode {
	1: Common.result result
	2: i32 length
	3: list<i32> data
}
struct convertInput {
	1: string srcFile
	2: string dstFile
}

