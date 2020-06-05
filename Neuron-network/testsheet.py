from main import Network

res = Network()

res.set_error(0.5)

res.print_data()
res.set_layer(3)
res.add_all_neuron([4, 4, 2])
res.create_network()
res.print_all()

res.learn([1, 0, 1, 0], [1, 0])

res.print_all()
res.print_last_layer()
