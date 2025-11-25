import logging
import sys
from pathlib import Path
from config import LOG_FILE

# Create a custom logger
logger = logging.getLogger("MonteWalk")

def setup_logging():
    """
    Configures the logging system for the entire application.
    Should be called once at application startup.
    """
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # File Handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    # Stream Handler (Console)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)

    # Configure Root Logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # Avoid adding duplicate handlers
    if not root_logger.handlers:
        root_logger.addHandler(file_handler)
        root_logger.addHandler(stream_handler)
    
    logger.info("Logging system initialized.")

def log_action(action_type: str, details: str) -> str:
    """
    Logs an agent action or reasoning step for audit purposes.
    
    Args:
        action_type: Category (e.g., 'REASONING', 'TRADE_DECISION', 'ERROR').
        details: Description of the action.
    """
    # Clean up details to remove excessive newlines or emojis if needed
    clean_details = details.strip()
    logger.info(f"[{action_type.upper()}] {clean_details}")
    return "Action logged successfully."
