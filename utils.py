def remove_prefix_word(message, remove_num_words=1):
    return " ".join(message.split()[remove_num_words:])

def read_config() -> dict:
    with open("config_bot.cfg", "r") as f:
        config_dict = {}

        for line in f:
            (key, val) = line.split()[0:2] # может измениться

            if val in ["True", "False"]:
                config_dict[key] = bool(val)

            elif val.isdigit():
                config_dict[key] = int(val)

            else:
                config_dict[key] = val
        
    return config_dict

  
def update_config(key, val):
    config_dict = read_config()

    if key in config_dict.keys():
        config_dict[key] = val
    else:
        print("there is no that key")

    with open("config_bot.cfg", "w") as f:
        for key in config_dict.keys():
            f.write(f"{key} {config_dict[key]} \n")