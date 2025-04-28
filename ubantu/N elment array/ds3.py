

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 16
elements_per_proc = N // size

# Only the root process initializes the array
if rank == 0:
    array = np.arange(1, N + 1, dtype='i')  # [1, 2, ..., 16]
else:
    array = None

# Create buffer for scattered data
sub_array = np.empty(elements_per_proc, dtype='i')

# Scatter data to all processes
comm.Scatter(array, sub_array, root=0)

# Compute local sum
local_sum = np.sum(sub_array)

print(f"Processor {rank} - Partial Sum: {local_sum}")

# Reduce local sums to the root process
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Total Sum: {total_sum}")



# sudo apt update
# sudo apt install mpich
# pip install mpi4py
# pip install numpy
# mpiexec -n 4 python3 sum_mpi.py
# output
# $ mpiexec -n 4 python3 sum_mpi.py
# Processor 0 - Partial Sum: 10
# Processor 1 - Partial Sum: 26
# Processor 2 - Partial Sum: 42
# Processor 3 - Partial Sum: 58
# Total Sum: 136

# pip3 install mpi4py --break-system-packages
