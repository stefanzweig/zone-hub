include "CommonNode.thrift"


service linParserNode {
	// 添加一个 DB 文件
	CommonNode.result addDbfile (1: CommonNode.filePath req)
	// 配置某个channel
	CommonNode.result setChannelConfig (1: CommonNode.linChannelConfigs req)
	CommonNode.result setNodeSimulation (1: linNodeConfig req)
	CommonNode.result setFrameSimulation (1: linFrameConfig req)
	CommonNode.result setFrameData(1:linFrameData req)
	CommonNode.result SetSignalData(1:linSignalData req)
	// 清除所有订阅
	CommonNode.result clearSubscribe ()
	//清空所有dbfile
	CommonNode.result clearDbfile ()
	// 获取状态
	linParserStatus getStatus ()
	linLdfJson getLdfJsonTree ()
	// 转换LinDb至python
	CommonNode.result convertLinDbToPy (1: convertInput req)
	// 转换LinDb至json
	CommonNode.result convertLinDbToJson (1: convertInput req)
	CommonNode.result setCrcConfig (1: linCrcConfigParser req)
	CommonNode.result clearCrcConfig (1: linCrcConfigParser req)
}
struct linNodeConfig {
	/**
	   string
	   	LIN节点名字
	*/
	1: string nodeName
	/**
	   int32
	   	LIN节点所在的软件通道
	*/
	2: i32 channel
	/**
	   bool
	   	LIN节点是否仿真标志位
	*/
	3: bool simu
}
struct linFrameConfig {
	/**
	   int32
	   	LIN报文ID信息
	*/
	1: i32 frameId
	/**
	   string
	   	LIN报文名字
	*/
	2: string frameName
	/**
	   int32
	   	LIN报文所在软件通道信息
	*/
	3: i32 channel
	/**
	   bool
	   	LIN报文是否仿真标志位
	*/
	4: bool simu
}
struct linFrameData {
	/**
	   int32
	   	LIN报文ID
	*/
	1: i32 frameId
	/**
	   string
	   	LIN报文名字
	*/
	2: string frameName
	/**
	   int32
	   	LIN报文所在软件通道信息
	*/
	3: i32 channel
	/**
	   string
	   	LIN数据，例如{sig1:1,sig2:1},然后使用json.dumps转换成string
	*/
	4: string setData
	/**
	   string
	   	LIN数据序列化方式，支持两种 'raw','unraw'
	*/
	5: string encodeType
}
struct linSignalData {
	/**
	   string
	   	LIN信号名字
	*/
	1: string signalName
	/**
	   int32
	   	LIN报文所在软件通道信息
	*/
	2: i32 channel
	/**
	   string
	   	LIN数据，使用json.dumps转换成string
	*/
	3: string setData
	/**
	   string
	   	LIN数据序列化方式，支持两种 'raw','unraw'
	*/
	4: string encodeType
}

struct linParserStatus {
	// 表达 LinParser 的状态
	// TODO 邢潇 根据实际情况调整
	1: CommonNode.result result
	2: i32 status
	3: string strStatus
}

struct linLdfJson {
	/**
	   int32
	   	返回值，0是成功，非0是失败
	*/
	1: i32 result
	/**
	   string
	   	失败的理由
	*/
	2: string reasonbinary
	/**
	   string
	   	成功后json数据
	*/
	3: string jsonData
}

struct convertInput {
	/**
	   string
	   	源文件地址
	*/
	1: string srcFile
	/**
	   string
	   	目标文件地址
	*/
	2: string dstFile
}

struct linCrcConfigParser {
	/**
	   int32
	   	需要设置CRC报文所在软件通道
	*/
	1: i32 channel
	/**
	   int32
	   	需要设置CRC报文ID
	*/
	2: i32 frameId
	/**
	   string
	   	需要设置CRC报文名字
	*/
	3: string frameName
	/**
	   string
	   	需要设置RC信号
	*/
	4: string signalRcName
	/**
	   string
	   	需要设置CRC信号
	*/
	5: string signalCrcName
	/**
	   int32
	   	需要设置RC最小值
	*/
	6: i32 rcMin
	/**
	   int32
	   	需要设置RC最大值
	*/
	7: i32 rcMax
	/**
	   list[int32]
	   	CRC table
	*/
	8: list<i32> crcTable
	/**
	   int32
	   	RC步长设置
	*/
	9: i32 stepLen
}
