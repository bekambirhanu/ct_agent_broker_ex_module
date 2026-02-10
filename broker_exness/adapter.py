import httpx
from shared.shared.interfaces.broker import BaseBroker
from shared.shared.config.Settings import Settings
from ct_agent_nlp_parser_module.nlp_parser.schema import TradeOrder

class ExnessBroker(BaseBroker):
    def __init__(self):
        self.bridge_url = Settings.MT5_BRIDGE_URL

    async def execute_order(self, order: TradeOrder) -> dict:
        payload = order.model_dump()
        # Add Exness specific credentials for the bridge to use
        payload.update({
            "login": Settings.MT5_LOGIN,
            "password": Settings.MT5_PASSWORD,
            "server": Settings.MT5_SERVER
        })

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.bridge_url}/trade", 
                    json=payload,
                    timeout=10.0
                )
                return response.json()
            except Exception as e:
                return {"success": False, "error": str(e)}

    def get_account_info(self):
        # Similar logic to call bridge /account endpoint
        pass