# 🔍 Tavily Search & Web Viewer

Simple and powerful extension for searching web and viewing website content.

## What can it do?

- Search anything on the web
- View any website content

## Setup
<picture>
  <source srcset="https://raw.githubusercontent.com/qwersyk/Newelle-tavily/master/screenshots/1w.png" media="(prefers-color-scheme: light)">
  <source srcset="https://raw.githubusercontent.com/qwersyk/Newelle-tavily/master/screenshots/1b.png" media="(prefers-color-scheme: dark)">
  <img src="https://raw.githubusercontent.com/qwersyk/Newelle-tavily/master/screenshots/1w.png" alt="settings" />
</picture>

1. Get your API key at [tavily.com](https://tavily.com)
2. Open extension settings

<div align="center">
  <div class="carousel">
    <picture>
      <source srcset="https://raw.githubusercontent.com/qwersyk/Newelle-tavily/master/screenshots/2w.png" media="(prefers-color-scheme: light)">
      <source srcset="https://raw.githubusercontent.com/qwersyk/Newelle-tavily/master/screenshots/2b.png" media="(prefers-color-scheme: dark)">
      <img src="https://raw.githubusercontent.com/qwersyk/Newelle-tavily/master/screenshots/2w.png" alt="search" />
    </picture>
    <picture>
      <source srcset="https://raw.githubusercontent.com/qwersyk/Newelle-tavily/master/screenshots/3w.png" media="(prefers-color-scheme: light)">
      <source srcset="https://raw.githubusercontent.com/qwersyk/Newelle-tavily/master/screenshots/3b.png" media="(prefers-color-scheme: dark)">
      <img src="https://raw.githubusercontent.com/qwersyk/Newelle-tavily/master/screenshots/3w.png" alt="website" />
    </picture>
  </div>
</div>

<style>
.carousel {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
    padding: 10px 0;
}

.carousel img {
    flex: 0 0 auto;
    width: 300px;
    height: 200px;
    margin-right: 15px;
    scroll-snap-align: start;
    border-radius: 8px;
    object-fit: cover;
}

.carousel::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}

.carousel::-webkit-scrollbar-thumb {
    background: #666;
    border-radius: 10px;
}

.carousel::-webkit-scrollbar-track {
    background: #ddd;
    border-radius: 10px;
}
</style>