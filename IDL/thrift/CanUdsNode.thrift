include "CommonNode.thrift"

service canUdsNode {
	CommonNode.result subscribe (1: node_info req)
	kvlist generate_key (1: request_para req)
	CommonNode.result diag_request(1: can_diag_message req)
	CommonNode.result diag_response(1: can_diag_message req)
}

struct can_diag_message {
  /**
	   int32
	   	诊断报文的ID
	*/
  1: i32 id
  /**
	   list[int16]
	   	诊断报文命令
	*/
  2: list<i16> cmd
  /**
	   int32
	   	诊断报文的DLC
	*/
  3: i8 dlc
  /**
	   bool
	   	诊断报文是否是FD
	*/
  4: bool is_fd
}

struct node_info {
  /**
	   int32
	   	节点物理寻址
	*/
  1: i32 request_id_phys
  /**
	   int32
	   	节点诊断响应地址
	*/
  2: i32 response_id
  /**
	   int32
	   	节点诊断功能寻址
	*/
  3: i32 request_id_func
  /**
	   int32
	   	节点所在通道信息
	*/
  4: i32 channel
}

struct request_para {
  /**
	   list[int32]
	   	解锁seed key列表
	*/
  1: list<i32> seed_value
  /**
	   int32
	   	解锁算子，每个ECU都有特定
	*/
  2: i32 algorithm_number
}

struct kvlist {
  /**
	   list[int32]
	   	用于解锁，计算后的key值列表
	*/
  1: list<i32> key_value
}