import os
from processors import transform_a, transform_b

def main() -> int:
    """
    main関数
    Returns:
        int: _description_
    """
    
    product_a = 100
    product_b = 200
    
    transform_a(product_a)
    transform_b(product_b)
    
    return 0

if __name__ == "__main__":
    main()    
    