
"""
_pdf2md_solo.py

Convert the GitCom reference PDF into Markdown
using PyMuPDF4LLM.

@ Solo Converting Version
"""

from pathlib import Path

import pymupdf4llm as pf4llm


# Resolve GitCom repository root from script location.
GC_ROOT = Path(__file__).resolve().parents[2]

# Reference material directories.
HAIR_DIR = GC_ROOT / "__hair_gitcom"
PDF_DIR = HAIR_DIR / "_prim_material"
MD_DIR = HAIR_DIR / "_llm_grasp"

# Target PDF.
PDF_PATH = (
    PDF_DIR
    / "NFAI_App_EC_Version_Beta_0.90.35.30_GLIMPSE.pdf"
)

MD_PATH = MD_DIR / PDF_PATH.with_suffix(".md").name


def main():
    if not PDF_PATH.is_file():
        raise FileNotFoundError(
            f"Reference PDF not found: {PDF_PATH}"
        )

    MD_DIR.mkdir(parents=True, exist_ok=True)

    markdown = pf4llm.to_markdown(str(PDF_PATH))

    MD_PATH.write_text(
        markdown,
        encoding="utf-8"
    )

    print(f"[OK] {PDF_PATH} -> {MD_PATH}")


if __name__ == "__main__":
    main()
