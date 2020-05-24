import os


def export_learning_history_to_csv(csv_file_path, fit_result, times):
    csv_file_dir = os.path.dirname(csv_file_path)
    if not os.path.exists(csv_file_dir):
        os.makedirs(csv_file_dir)

    content = f'epoch,time,val_loss,val_accuracy,val_precision,val_recall,loss,accuracy,precision,recall\n'
    content = content + '0,0,0,0,0,0\n'

    for epoch in fit_result.epoch:
        content = content + f'{epoch + 1},' \
                            f'{times[epoch]},' \
                            f'{fit_result.history["val_loss"][epoch]},' \
                            f'{fit_result.history["val_accuracy"][epoch]},' \
                            f'{fit_result.history["val_precision"][epoch]},' \
                            f'{fit_result.history["val_recall"][epoch]},' \
                            f'{fit_result.history["loss"][epoch]},' \
                            f'{fit_result.history["accuracy"][epoch]},' \
                            f'{fit_result.history["precision"][epoch]},' \
                            f'{fit_result.history["recall"][epoch]}\n'

    print(content)
    csv_file = open(csv_file_path, 'w')
    csv_file.write(content)
    csv_file.close()


def export_learning_validation_result_to_csv(csv_file_path, result, times):
    csv_file_dir = os.path.dirname(csv_file_path)
    if not os.path.exists(csv_file_dir):
        os.makedirs(csv_file_dir)

    content = f'avg_epoch_time,time,val_loss,val_accuracy,val_precision,val_recall\n'
    content = content + f'{sum(times) / len(times)},' \
                        f'{sum(times)},' \
                        f'{result[0]},' \
                        f'{result[1]},' \
                        f'{result[2]},' \
                        f'{result[3]}'

    print(content)
    csv_file = open(csv_file_path, 'w')
    csv_file.write(content)
    csv_file.close()
