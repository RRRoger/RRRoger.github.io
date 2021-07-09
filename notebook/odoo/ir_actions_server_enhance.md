# ir_actions增强

> `ir.actions.server`添加`json_dumps`函数

```python
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.base.ir.ir_actions import IrActionsServer
import json

CODE_DESC_HEAD = """# Add IN module ir_actions_enhance
#  - json_dumps from json: Python libraries
# ******
"""


class IrActionsServerExtends(models.Model):
    _inherit = 'ir.actions.server'

    DEFAULT_PYTHON_CODE = CODE_DESC_HEAD + IrActionsServer.DEFAULT_PYTHON_CODE
    code = fields.Text(default=DEFAULT_PYTHON_CODE)

    @api.model
    def _get_eval_context(self, action=None):
        """
            add json.dumps
            add base64.b64encode
            add base64.b64decode
        :param action:
        :return:
        """
        res_data = super(IrActionsServerExtends, self)._get_eval_context(action=action)
        res_data['json_dumps'] = json.dumps
        return res_data
```

