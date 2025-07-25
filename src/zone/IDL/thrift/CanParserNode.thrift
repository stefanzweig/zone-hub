// Version = 1.0.20220202
include "CommonNode.thrift"
include "CanStackNode.thrift"



service canParserNode {
	CommonNode.result checkAlive()

    CommonNode.result setCrcRcConfig (1: pduCrcRcConfig req)

    CommonNode.result clearAllCrcRcConfig ()

    CommonNode.result clearCrcRcConfig (1: pduCrcRcConfig req)

    CommonNode.result sendCanFrameCyc (1: CanStackNode.canMessage req)

    CommonNode.result sendCanPduCyc (1: pduMessage req)

    CommonNode.result sendCanPduCycList (1: pduMessages req)

    CommonNode.result sendCanPdu (1: pduMessage req)

	CommonNode.result addDbFile (1: dbPath req)
	
	CommonNode.result setConfig (1: dbConfigs req)

	dbConfigs getCanDbConfigs ()

	dbPath getCanDbPath ()

    CommonNode.result subscribeMsg (1: subscribeInfo req)

    CommonNode.result unSubscribeMsg (1: subscribeInfo req)
    
    canDbInfo getCanDbInfo ()

	CommonNode.result clear ()

	CommonNode.result clearSubscribe ()

	iSignalIPduEncode encodePdu (1: iSignalIPduObj req)

	CommonNode.result convertCanDbToPy (1: convertInput req)

	CommonNode.result convertCanDbToJson (1: convertInput req)

    CommonNode.result updateCanPdu (1: pduUpdate req)
}

/**
 *
 *PDU crc和rc配置信息结构体
 *
 */
struct pduCrcRcConfig {
	/**
	   int32
	   	需要设置的pdu的软件通道信息
	*/
	1: i32 channel
	/**
	   string
	   	需要设置的pdu的名字
	*/
	2: string pduName
	/**
	   int32
	   	该字段是可选参数，如知晓crc的信号名可填下方crcName
	   	crc起始位信息
	*/
	3: optional i32 crcBitStarts 
	/**
	   int32
	   	该字段是可选参数，如知晓rc的信号名可填下方rcName
	   	rc起始位信息
	*/
	5: optional i32 rcBitStarts 
	/**
	   list[int8]
	   	该字段是可选参数，如不填默认使用crc8表
	   	crc对应表信息
	*/
	7: optional list<i32> crcTable
	/**
	   int32
	   	该字段是可选参数，如知晓crc的起始位可填上方crcBitStarts
	   	crc信号名字
	*/ 
	8: optional string crcName
	/**
	   int32
	   	该字段是可选参数，如知晓rc的起始位可填上方rcBitStarts
	   	rc信号名字
	*/
	9: optional string rcName
	/**
	   list[int32]
	   	rc配置信息为列表，长度>=3，例如[0,14,2]，0代表counter最小值，14代表最大值，步长为2，对应couter值变化0,2,4,6,8,10,12,14,0...
	*/
	10: list<i32> rcConfig
}

/**
 *
 *PDU 填充位赋值信息结构
 *
 */
struct paddingBitInfo{
	/**
	   int32
	   	填充位MSB起始位置
	*/
	1: i32 msbStartBit
	/**
	   int32
	   	需要填充位长度，就是从起始位开始需要多少个位被赋值
	*/
	2: i32 bitLen
	/**
	   int64
	   	这些填充位需要被赋予的值，按bit来看
	*/
    3: i64 value
}

/**
 *
 *PDU 更新值信息结构体
 *
 */
struct pduUpdate{
	/**
	   int32
	   	更新pdu对象所在的软件通道信息
	*/
	1: i32 channel
	/**
	   int32
	   	更新pdu对象名字
	*/
	2: string pduName
	/**
	   list[int32]
	   	可选参数，可以选择直接更新原始值
	   	更新pdu对象原始值,如[1,2,3,4,5,6,7,8]
	*/
    3: optional list<i32> data = []
	/**
	   string
	   	可选参数，可以选择直接更新信号值，其中信号值为phy
	   	更新pdu对象中信号值，例如{'siga'：'ON'，'sigb':17.5},然后将该字典json dumps至string传递
	*/
    4: optional string context = ''
	/**
	   string
	   	可选参数，可以选择直接更新信号值，其中信号值为raw
	   	更新pdu对象中信号值，例如{'siga'：1，'sigb':0},然后将该字典json dumps至string传递
	*/
    5: optional string context_raw = ''
	/**
	   paddingBitInfo
	   	更新pdu对象中填充位信息，同时也可以更新有信号填充位，该参数优先级高于context值
	*/
    6: list<paddingBitInfo> padding_bit_list = []
}

/**
 *
 *单条PDU发送信息
 *
 */
struct pduMessage {
	/**
	   int32
	   	发送pdu对象所在的软件通道信息
	*/
	1: i32 channel
	/**
	   string
	   	发送pdu对象名字
	*/
	2: string pduName
	/**
	   int32
	   	发送pdu周期，单位ms
	*/
	3: i32 period
	/**
	   int32
	   	发送pdu次数
	*/
    4: optional i32 times

}


/**
 *
 *多条PDU发送信息
 *
 */
struct pduMessages{
	/**
	   list[pduMessage]
	   	发送pdu列表，元素为本文件中pduMessage结构体
	*/
    1:list<pduMessage> message
}

/**
 *
 *CAN解析节点订阅信息结构体
 *
 */
struct subscribeInfo {
	/**
	   int32
	   	发送订阅对象所在的软件通道信息
	*/
	1: i32 channel
	/**
	   string
	   	发送订阅对象名字，可以是信号名，PDU名字，Frame的名字
	*/
	2: string name
	/**
	   string
	   	发送订阅对象类型，可以'message','frame','signal','pdu'
	*/
	3: string type
	/**
	   int32
	   	发送订阅对象类型为'message'时，需要设置该参数为对应报文的ID
	*/
	4: i32 frameId
}

/**
 *
 *CAN数据库路径
 *
 */
struct dbPath {
	/**
	   CommonNode.result
	   	该参数历史原因，保留，不用赋值
	*/
	1: CommonNode.result result
	/**
	   string
	   	数据库文件绝对路径
	*/
	2: string dbPath
}

/**
 *
 *ARXML 每路CAN配置软件通道
 *
 */
struct dbConfigs {
	/**
	   CommonNode.result
	   	该参数历史原因，保留，不用赋值
	*/
	1: CommonNode.result result
	/**
	   list[dbConfigPair]
	   	所有软件通道与arxml中通道匹配，元素该文件中的dbConfigPair结构体
	*/
	2: list<dbConfigPair> configs
}

/**
 *
 *ARXML 单路CAN配置软件通道
 *
 */
struct dbConfigPair {
	/**
	   int32
	   	软件通道信息
	*/
	1: i32 channel
	/**
	   string
	   	对应软件通道需要赋与ARXML信息，如BDCAN
	*/
	2: string dbName
}

/**
 *
 *CAN arxml信息
 *
 */
struct canDbInfo {
	/**
	   CommonNode.result
	   	请求状态返回值，发送时不需要赋值
	*/
	1: CommonNode.result result
	/**
	   string
	   	返回当前设置的arxml后解析的值，该值为字符串，json.loads()后为需要的字典
	*/
	2: string strJson
}

struct iSignalIPduObj {
	1: i32 channel
	2: string pduName
	3: string pduContext
}
struct iSignalIPduEncode {
	1: CommonNode.result result
	2: i32 length
	3: list<i32> data
}

/**
 *
 *arxml转换py,json入参
 *
 */
struct convertInput {
	/**
	   string
	   	源文件地址，绝对路径
	*/
	1: string srcFile
	/**
	   string
	   	目标文件地址，绝对路径
	*/
	2: string dstFile
}

