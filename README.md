### Generate gRPC code
```
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/agent_service.proto
```

### Build Package
```
python -m build
```


### Upload Package
```
py -m twine upload dist/*
```