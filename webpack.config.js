var path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
var AssetsPlugin = require('assets-webpack-plugin');

module.exports = {
    entry: {
      ux: "./src/index.js",
      design: "./scss/main.scss"
    },
    output: {
      path: path.resolve(__dirname, 'static'),
      publicPath: "/static/",
      filename: '[name].[chunkhash].js'
    },
    module: {
        rules: [
          {
            test: /\.s[c|a]ss$/,
            use: [
              'style-loader',
              MiniCssExtractPlugin.loader,
              'css-loader',
              'sass-loader']
          },
          {
            test: /\.m?js$/,
            exclude: /(node_modules|bower_components)/,
            use: {
              loader: 'babel-loader',
              options: {
                presets: ['@babel/preset-env']
              }
            }
          }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin(),
        new AssetsPlugin()
    ]
};
