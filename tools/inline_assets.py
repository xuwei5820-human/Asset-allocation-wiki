"""把 HTML 中引用的本機圖片內嵌成 data URI，輸出單一 HTML 檔。

用法：
    py -I tools/inline_assets.py <來源.html> <輸出.html>

- 只處理本機相對路徑（src="..."、url(...)），http/https 連結不動
- 路徑以來源 HTML 所在資料夾為基準
"""
import base64
import mimetypes
import pathlib
import re
import sys

PATTERN = re.compile(r"""(src=["']|url\(["']?)([^"')]+?\.(?:jpe?g|png|webp|gif|svg))(["')])""", re.I)


def inline(src: pathlib.Path, out: pathlib.Path) -> None:
    html = src.read_text(encoding="utf-8")
    cache: dict[str, str] = {}

    def repl(m: re.Match) -> str:
        ref = m.group(2)
        if ref.startswith(("http://", "https://", "data:")):
            return m.group(0)
        if ref not in cache:
            path = (src.parent / ref).resolve()
            mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            cache[ref] = f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()
        return m.group(1) + cache[ref] + m.group(3)

    result = PATTERN.sub(repl, html)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(result, encoding="utf-8")
    print(f"{out}  ({len(cache)} images, {out.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    inline(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]))
