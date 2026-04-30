import httpx
from shared.shared.interfaces.broker import BaseBroker
from shared.shared.config.Settings import Settings
from nlp_parser.schema import TradeOrder
from .constants import mt5

class ExnessBroker(BaseBroker):
    def __init__(self, login: str, password: str, server: str):
        self.bridge_url = Settings.MT5_BRIDGE_URL
        self._login = login
        self._password = password
        self._server = server

    async def execute_order(self, order: TradeOrder) -> dict:
        payload = order.model_dump()
        
        action: int = mt5.TRADE_ACTION_DEAL if payload.get('order_type').upper() == "MARKET" else mt5.TRADE_ACTION_PENDING
        
        # Additional constants and configurations
        print(payload)

        # Add user-specific MT5 credentials for the bridge
        payload.update({
            "login": self._login,
            "password": self._password,
            "server": self._server
        })

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.bridge_url}/trade",
                    headers={"x_token":Settings.BRIDGE_SECRET_TOKEN},
                    json=payload,
                    timeout=10.0
                )
                return response.json()
            except (httpx.HTTPError, httpx.HTTPStatusError) as e:
                return {"success": False, "error": str(e)}
            except Exception as e:
                return { "success": False, "error": str(e)}

    def get_account_info(self):
        # Similar logic to call bridge /account endpoint
        pass