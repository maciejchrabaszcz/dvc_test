import dvclive

for i in range(10):
    dvclive.log('acc', i**(0.5))
    dvclive.log('loss', -i**(1.5))
    dvclive.next_step()

