# k9s
[k9s commands](https://k9scli.io/topics/commands/)
* d = describe
* l = logs
* :ctx = switch context
* :ns = switch namespace
* ctrl-w = wide columns

# k8s
* [k8s cheatsheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

```bash
# list things
# flags: -n (pass in namespace), -A (all namespaces)
kubectl get pods -o wide # more detailed list
kubectl get nodes
kubectl get secrets
kubectl get services # --sort-by=.metadata.name to sort by name

# describe things
kubectl describe pods podname -n namespace
kubectl describe nodes nodename -n namespace

# start a shell (with 1 container)
kubectl exec -it podname -n namespace -- /bin/sh

# stream pod logs
kubectl logs podname -n namespace
# add -c containername if multi-container pod
# add -f to stream logs

# get events sorted by timestamp
kubectl get events --sort-by=.metadata.creationTimestamp
```

# helm
```bash
# check deployed values
helm get values releasename -n namespace
```
