include "CommonNode.thrift"



service logReplayNode {
	
	CommonNode.result startLog (1: logRequest req)
	
	CommonNode.genericString getLogStatus ()
	
	CommonNode.result stopLog (1: logRequest req)
	
	CommonNode.result addLinDecodeRole (1: CommonNode.genericString req)
	
	CommonNode.result addCanDecodeRole (1: CommonNode.genericString req)

	CommonNode.result addSomeIpDecodeRole (1: CommonNode.genericString req)

	CommonNode.result addDDSDecodeRole (1: CommonNode.genericString req)
	
	decodeResult replayNextN (1: decodeN req)
	
	CommonNode.result openReplayFile (1: CommonNode.filePath req)
	
	CommonNode.result closeReplayFile (1: CommonNode.filePath req)
	
	CommonNode.genericString getReplayStatus ()
	
	CommonNode.result reset ()
	
}
struct linMessageDecode {
	1: CommonNode.result result
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
	1: CommonNode.result result
	2: i32 startIndex
	3: i32 stopIndex
	4: bool isStop
}

struct logRequest {
	/**
	   CommonNode.filePath
	   	文件的地址，类型为通用节点中filePath类型
	*/
	1: CommonNode.filePath filePath
	/**
	   int32
	   	预留参数，不用赋值
	*/
	2: i32 logFlag
}

