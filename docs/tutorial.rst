============
简易教程
============

例子一
============

.. code:: python

    # import the library
    from zone import App
    from zone.dsc import DbPath, CanMessage, CanChannelConfig

    # define the app
    app = zone.App()

    # connect the can-related components
    result = app.connect(["canstack", "canparser"])

    # add db file
    app.addCanDbFile(r'E:\Shared\WORKS\codebase\xxx.arxml')

    # set channel config
    config = CanChannelConfig()
    # set the parameters of the config
    # ...
    app.setCanChannelConfig([config])

    # start stack
    app.start(["canstakck", "canparser"])

    # send can message
    can_msg = CanMessage(channel=0,
                         isFd=False,
                         id=1,
                         dlc=8,
                         isExtended=True,
                         isRemote=False,
                         data=[1, 2, 3, 4, 5],
                         period=100,
                         frameName="frame",
                         times=10)
    app.sendCanMessage(can_msg)

    # disconnect the can-related components
    result = app.disconnect(["canstack", "canparser"])
