# Neural Love API Python Wrapper

This is a Python API wrapper for the neural.love API.

## Features

- Generate AI art.
- Check order status.
- Estimate generation cost.

## Installation

Soon to be available on PyPI:

```bash
pip install neural-love-api
```

Create an instance of the API wrapper.

```python
api = NeuralLoveAPI(api_key="your-api-key")
```

Generate art.

```python 
api.generate_art(
    prompt="a cat", 
    style="painting", 
    layout="square", 
    amount=1,
    is_hd=False,
    is_public=True
)
```

Check order status.
```python
api.get_order_status(order_id="order-id")
```

Estimate generation cost.
```python
api.estimate_cost(
    prompt="a cat", 
    style="painting", 
    layout="square", 
    amount=1,
    is_hd=False,
    is_public=True
)
```

## Contributing
Pull requests are welcome.
