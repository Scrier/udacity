import numpy as np

output_error_term = np.array([-0.05163568, -0.05031333])
hidden_outputs = np.array([0.4850045, 0.45512111])
delta_weights_h_o = np.array([[0.0],[0.0]])

print(output_error_term.shape)
print(hidden_outputs.shape)
print(delta_weights_h_o.shape)

delta_weights_h_o +=  output_error_term[:,None] * hidden_outputs[:,None]

print(delta_weights_h_o)
