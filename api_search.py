from quart import Quart, jsonify, request
from p1337x import py1337x

app = Quart(__name__)
search_engine = py1337x(proxy='1337xx.to', cache='py1337xCache', cacheTime=500)


@app.route('/search', methods=['GET'])
async def search():
    query = request.args.get('query')
    if query != '':
        search_results = search_engine.search(query)
    else:
        search_results = search_engine.trending()
    return jsonify(search_results), 200


@app.route('/get_info', methods=['GET'])
async def get_info():
    link = request.args.get('link')
    a = search_engine.info(link=link)
    return jsonify(a), 200


@app.route('/health', methods=['GET'])
async def check_health():
    a = {"status": "Fine!"}
    return jsonify(a), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
