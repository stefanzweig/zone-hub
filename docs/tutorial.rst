============
简易教程
============

例子一
============

.. code:: python

    # import the library
    import zone
    from zone.dsc import DbPath, CanMessage

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
    can_msg = CanMessage(channel=channel,
                         isFd=is_fd,
                         id=arbitration_id,
                         dlc=dlc,
                         isExtended=is_extended_id,
                         isRemote=is_remote_frame,
                         data=data,
                         period=period_ms,
                         frameName=name,
                         times=times)
    app.sendCanMessage(can_msg)

    # disconnect the can-related components
    result = app.disconnect(["canstack", "canparser"])
