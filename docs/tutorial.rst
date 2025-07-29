====
教程
====

例子
====

.. code:: python

    # import the library
    import zone
    from zone.dsc import DbPath
    from zone.dsc import CanMessage

    # define the app
    app = zone.App()

    # connect the can-related components
    result = app.connect(["canstack", "canparser"])

    # add db file
    app.addCANDbFile(r'E:\Shared\WORKS\codebase\xxx.arxml')

    # set channel config
    # # construct configs
    app.setCanChannelConfig(configs)

    # start stack
    app.start(["canstakck", "canparser"])

    # send can message
    can_msg = CanMessage(hannel=obj.channel, isFd=obj.is_fd, id=obj.arbitration_id, dlc=obj.dlc, isExtended=obj.is_extended_id,
	     isRemote=obj.is_remote_frame, data=obj.data, period=period_ms, frameName=obj.name, times=times)
    app.sendCanMessage(can_msg)

    # disconnect the can-related components
    result = app.disconnect(["canstack", "canparser"])
