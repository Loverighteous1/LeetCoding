
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    new_id = []
    id_ = weather.id
    temp_ = weather.temperature
    print(type(id_))
    print(type(temp_))
    for ind in range(len(temp_)-1):
        if temp_[ind] < temp_[ind+1]:
            new_id.append(id_[ind + 1])

    new_id = pd.DataFrame({'id':new_id})
    return new_id