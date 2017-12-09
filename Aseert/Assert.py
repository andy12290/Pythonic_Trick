# This is related to assert statment

def apply_discount(product,discount):
    discount_price = int(product['price'] * (1-discount))
    return discount_price

# test
shoes = {'name': 'Fancy Shoes', 'price': 14900}
print(apply_discount(shoes,0.25))
# output 11175

print(apply_discount(shoes,2.0))
# out: -14900

# we have to check the condition it should not go beyind the original discount_price

def apply_discount_assert(product,discount):
    discount_price = int(product['price'] * (1-discount))
    assert 0 <= discount_price <= product['price']
    return discount_price

#def apply_discount(product,discount):
'''
discounted prices calculated by this function cannot be lower than $0 and they
cannot be higher than the original price of the product.
'''

print(apply_discount_assert(shoes,2.0))
# it will generate the assert statement.
# its good for debugging but not for the data validation.
