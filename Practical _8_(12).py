# Store product name and quantity
inventory = {
    "Laptop": 10,
    "Mouse": 21,
    "keyword": 17
}  #[span_0](start_span)[span_0](end_span)

# Add product
inventory["Monitor"] = 5  #[span_1](start_span)[span_1](end_span)

# Update stock
inventory["Mouse"] = 30  #[span_2](start_span)[span_2](end_span)

# Remove product
inventory.pop("keyword")  #[span_3](start_span)[span_3](end_span)

# Display final inventory
print("Final inventory:")  #[span_4](start_span)[span_4](end_span)
for product, quantity in inventory.items():  #[span_5](start_span)[span_5](end_span)
    print(product, ":", quantity)  #[span_6](start_span)[span_6](end_span)
