"""import logging

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename = "pipeline.log",
        filemode = 'a'   ###"a" for append, "w" for overwrite
)

logging.debug("Debug message")
logging.info("Pipeline started")
logging.warning("One invalid row was rejected")
logging.error("Database connection failed")
logging.critical("Pipeline cannot continue")"""

"""import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s',
    filename='pipeline.log',
    filemode='a'  # "a" for append, "w" for overwrite
)
order_id = "102"
quantity = "abc"

try:
    quantity = int(quantity)
    
except ValueError as err:
    ###logging.warning("Invalid quantity encountered")
    from tkinter.messagebox import WARNING


logging.warning( "Order %s rejected: %s",
                    order_id,
                    err))
    ###The %s placeholders are filled with order_id and the exception message. The log will look approximately like this:
    ###WARNING - Order 102 rejected: invalid literal for int() with base 10: 'abc'
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='pipeline.log',
    filemode='a' 
)

orders = [
    {"order_id": "101", "quantity": "3"},
    {"order_id": "102", "quantity": "abc"},
    {"order_id": "103", "quantity": "-2"}, 
    {"order_id": "104", "quantity": "5"}  
]

valid_count = 0
rejected_count = 0

logging.info("Pipeline started")

for order in orders:
    try:
        quantity = int(order["quantity"])
        
        if quantity <= 0:
            raise ValueError("Quantity must be a positive")

    except ValueError as err:
        rejected_count += 1
        logging.warning("Order %s rejected: %s", order["order_id"], err)

    else:
        valid_count += 1
        logging.info("Order %s processed successfully", order["order_id"])


logging.info("Valid orders: %d", valid_count)
logging.info("Rejected orders: %d", rejected_count)
logging.info("Pipeline finished")


"""
try:
    connect_to_database()
except Exception:
    logging.exception("Database connection error")"""
###logging.exception(): Records an error message and the traceback for the active exception. It is normally used inside an except block to help diagnose unexpected failures.