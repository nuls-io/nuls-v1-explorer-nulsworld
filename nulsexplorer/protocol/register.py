
# We will register here handlers for the tx types
TX_TYPES_REGISTER = dict()

# We will register here processors for the tx by types
TX_PROCESSOR_REGISTER = dict()

def register_tx_type(tx_type, handler_class):
    TX_TYPES_REGISTER[tx_type] = handler_class
