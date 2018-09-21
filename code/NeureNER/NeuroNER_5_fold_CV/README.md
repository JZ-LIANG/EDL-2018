0. here just the code and training data for one fold 524 entities, it may take 3 days and need at least 2GB free disk storage.
   since you told me there is not a lot storage available, i divide the data like this to limite the storage required. 

   after the program finish, share me the folder "NeuroNER_5_fold_CV/data/RPI/fold*_large", i have writen code to processing the result.




1. first copy the whole "NeuroNER_5_fold_CV" folder to a directory with at least 2GB free disk storage.


2. environment:

linux OS
python3
tensorflow 1.0, CPU version.

other package need:
you can run the "install_ubuntu.sh" in the to install part of them. 



3. run the "run.sh" in the "NeuroNER_5_fold_CV"



4. after each entity was trained, in the stdout(terminal screen) it will print the curent progress "n / 524 entities is done".
   use it to check progress, if it is too slow, we may need to change the stop metric again.
