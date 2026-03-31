from enum import Enum


class mt5(Enum):
    """
    A class for some metatrade constants
    """
    # Order Types
    ORDER_TYPE_BUY: int = 0 #Market Buy Order
    ORDER_TYPE_SELL: int = 1 #Market Sell Order
    ORDER_TYPE_BUY_LIMIT: int = 2 #Buy Limit
    ORDER_TYPE_SELL_LIMIT: int = 3 #Sell Limit
    ORDER_TYPE_BUY_STOP: int = 4 #Buy Stop
    ORDER_TYPE_SELL_STOP: int = 5 #Sell Stop
    ORDER_TYPE_BUY_STOP_LIMIT: int = 6 #Buy Stop Limit
    ORDER_TYPE_SELL_STOP_LIMIT: int = 7 #Sell Stop Limit 

    # Trade Action
    TRADE_ACTION_DEAL: int = 1 #Place order for immediate execution (market order).
    TRADE_ACTION_PENDING: int = 2 #Place pending order.

    # Order Filling Types
    ORDER_TYPE_FILLING_FOK: int = 0 #Fill or Kill
    
    # Magic Number
    MAGIC: int = 123456