var path = require('path')
var webpack = require('webpack')
var autoprefixer = require('autoprefixer')
var ExtractTextPlugin = require('extract-text-webpack-plugin')
var scssLoader = ['css-loader', 'sass-loader']
var BROWSERSLIST_CONFIG = ['ios >= 8', 'android >= 4', 'safari >= 6', 'chrome >= 34']

var vendorList = [
  "jquery",
  "classnames"
]

module.exports = {
  entry: {
    base: './app/static/resource/common/base.js',
    index: './app/static/resource/index/index.js'
  },
  output: {
    path: path.resolve(__dirname, "./app/static/dist"),
    filename: "[name].js"
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        loader: ExtractTextPlugin.extract(scssLoader.join('!'))
      },
      {
        test: /\.js$/,
        loader: "babel-loader",
        query: {
          plugins: ['transform-decorators-legacy', 'transform-class-properties']
        }
      },
      {
        test: /\.(png|jpg|jpeg|gif)$/i,
        loader: 'url-loader?limit=250000'
      }
    ]
  },
  resolve: {
    modules: [
      './node_modules',
      './app/static/resource'
    ],
    extensions: [".js", ".jsx", ".json"]
  },
  target: 'web',
  plugins: [
    new ExtractTextPlugin('[name].css'),
    new webpack.optimize.CommonsChunkPlugin({
        names: ['vendor', 'manifest'],
        minChunks: Infinity
    })
  ]
}