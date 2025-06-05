include "Common.thrift"



service logReplayNode {
	/**
	 *
	 *    开始一个数据记录
	 *    绝对路径
	 *    log_request:
	 *        - log_flag: 要启动记录的标志位
	 *            - 0x01 << 0: CAN
	 *            - 0x01 << 1: LIN
	 *    result: 执行结果
	 *        - 0: 启动记录成功
	 *        - 1: 已经有一个记录任务在了
	 *        - 2: 文件已经存在
	 *        - 1000: raise
	 *    
	 */
	Common.result startLog (1: logRequest req)
	/**
	 *
	 *    获取当前的 Log 状态
	 *    
	 */
	Common.genericString getLogStatus ()
	/**
	 *
	 *    停止一个数据记录任务
	 *    result: 执行结果
	 *        - 0: 结束成功
	 *        - 1000: reise
	 *    
	 */
	Common.result stopLog (1: logRequest req)
	/**
	 *
	 *    添加 LIN 的解析规则
	 *    generic_string: {
	 *        'channels': list[int],    通道
	 *        'ldfs': list[str],    通道对应的 ldf  文件
	 *    }
	 *    
	 */
	Common.result addLinDecodeRole (1: Common.genericString req)
	/**
	 *
	 *    添加 CAN 的解析规则
	 *    generic_string: {
	 *        'can_db_filePath': str,    CAN Arxml 文件
	 *        'channels': list[int],    CAN 通道
	 *        'cluster_names': list[str],    CAN 通道对应的 CAN_Cluster 名字
	 *        'channel_id_filters': list[int],    要使能解包的 id
	 *    }
	 *    
	 */
	Common.result addCanDecodeRole (1: Common.genericString req)
	Common.result addSomeIpDecodeRole (1: Common.genericString req)
	Common.result addDDSDecodeRole (1: Common.genericString req)
	/**
	 *
	 *    反序列化下面 n 个数据
	 *    
	 */
	decodeResult replayNextN (1: decodeN req)
	/**
	 *
	 *    打开一个 blf 文件
	 *    
	 */
	Common.result openReplayFile (1: Common.filePath req)
	/**
	 *
	 *    关闭当前的 blf 文件
	 *    
	 */
	Common.result closeReplayFile (1: Common.filePath req)
	/**
	 *
	 *    获取 blf 文件的描述信息
	 *    
	 */
	Common.genericString getReplayStatus ()
	/**
	 *
	 *    复位
	 *    
	 */
	Common.result reset ()
	/**
	 *
	 *    解析blf并保存至DB
	 *    
	 */
	decodeResult parseToDb (1: decodeN req)
	/**
	 *
	 *    数据库dump
	 *    
	 */
	Common.result dbDump (1: Common.filePath req)
	/**
	 *
	 *    数据库restore
	 *    
	 */
	Common.result dbRestore (1: restoreParam req)
}
struct linMessageDecode {
	1: Common.result result
	2: i32 channel
	3: i32 id
	4: string decodeStr
}
struct linDecodeRole {
	1: list<i32> channels
	2: list<string> ldfs
}
struct canDecodeRole {
	1: string canDbFilePath
	2: list<i32> channels
	3: list<string> clusterNames
}
struct decodeN {
	1: string blfFilePath
	2: i32 count
}
struct decodeResult {
	1: Common.result result
	2: i32 startIndex
	3: i32 stopIndex
	4: bool isStop
}
struct blfFileInfo {
	1: Common.result result
	2: string fileInfo
}
struct logRequest {
	1: Common.filePath filePath
	2: i32 logFlag
}
struct restoreParam {
	1: string archive
	2: string nsTo
}
