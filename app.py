from flask import Flask, render_template
import shutil

app = Flask(__name__, static_url_path='/static')
destination_path = './1'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/move_file_p1_1', methods=['POST'])
def move_file11():
    source_path114 = './原神启动素材_P1_1版/1.mp4'
    source_path113 = './原神启动素材_P1_1版/1.mp3'

    try:
        shutil.copy(source_path114, destination_path)
        shutil.copy(source_path113, destination_path)
        return '<script> window.alert("修改成功");window.open("/");</script>'
    except Exception as e:
        return f'Error moving file: {e}'


@app.route('/move_file_p2_1', methods=['POST'])
def move_file21():
    source_path214 = './原神启动素材_P2_1版有音频版/1.mp4'
    source_path213 = './原神启动素材_P2_1版有音频版/1.mp3'

    try:
        shutil.copy(source_path214, destination_path)
        shutil.copy(source_path213, destination_path)
        return '<script> window.alert("修改成功");window.open("/");</script>'
    except Exception as e:
        return f'Error moving file: {e}'


@app.route('/move_file_p3_2', methods=['POST'])
def move_file32():
    source_path324 = './原神启动素材_P3_2版（植物大战僵尸音乐版）/1.mp4'
    source_path323 = './原神启动素材_P3_2版（植物大战僵尸音乐版）/1.mp3'

    try:
        shutil.copy(source_path324, destination_path)
        shutil.copy(source_path323, destination_path)
        return '<script> window.alert("修改成功");window.open("/");</script>'
    except Exception as e:
        return f'Error moving file: {e}'


@app.route('/move_file_p4_2', methods=['POST'])
def move_file42():
    source_path424 = './原神启动素材_P4_2版有音频（植物大战僵尸音乐版）/1.mp4'
    source_path423 = './原神启动素材_P4_2版有音频（植物大战僵尸音乐版）/1.mp3'

    try:
        shutil.copy(source_path424, destination_path)
        shutil.copy(source_path423, destination_path)
        return '<script> window.alert("修改成功");window.open("/");</script>'
    except Exception as e:
        return f'Error moving file: {e}'


if __name__ == '__main__':
    app.run(debug=True)
