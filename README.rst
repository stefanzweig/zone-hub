Zone-Hub
=============

安装方法
-------------

``pip install zone-hub``

参考用例
-------------------

.. code:: python

    # import the library
    from zone import App
    from zone.dsc import DbPath, CanMessage, CanChannelConfig

    # define the app
    app = App()

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
    can_msg = CanMessage(channel=1,
                         isFd=False,
                         id=1,
                         dlc=8,
                         data=[1, 2, 3, 4, 5, 6, 7, 8],
                         period=100,
                         frameName="frame",
                         times=10)
    app.sendCanMessage(can_msg)

    # disconnect the can-related components
    result = app.disconnect(["canstack", "canparser"])

参考文档
--------------------

参考文档可以在这里找到：`zone-hub.readthedocs.io <https://zone-hub.readthedocs.io/>`__.
