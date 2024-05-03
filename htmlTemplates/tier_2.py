HTML_TEMPLATE_LINEA_2 = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Outfit:100,200,300,regular,500,600,700,800%7CIBM+Plex+Sans+Hebrew:200,300,regular,500,600"
      media="all"
    />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      body {
            position: relative;
            display: flex;
            align-items: center;
            justify-content:center;
            overflow: hidden !important;
            background: transparent !important;
            margin: 0px !important
          
        }

      * {
        margin: 0px;
         overflow: hidden !important;
      }
      .container {
        font-family: "Outfit";
        position: relative;
        overflow: hidden;
        height: fit-content;
        width: 330px;
        background-color: #121212;
        border: 1px solid #505050;
      }
      .card_highlighted .footer {
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: rgba(29, 29, 29, 0.6);
        backdrop-filter: blur(10px);
      }
      .container > img:nth-child(1) {
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
      .container .bg_image {
        width: 100%;
        height: 100%;
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        position: absolute;
        top: 0;
        left: 0;
      }
      .card_highlighted .divider {
        border-radius: 1000px;
        background: rgba(255, 255, 255, 0.25);
      }
      .container .metal_border {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        object-fit: cover;
      }
      .container .content_container {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 14px;
        position: relative;
        z-index: 3;
      }
      .content_container .cover_image {
        width: 100%;
        object-fit: cover;
        object-position: top;
        margin-bottom: 12px;
      }
      .content_container .chain_section {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        width: 100%;
        justify-content: space-between;
        margin-bottom: 12px;
      }
      .content_container .chain_section > img:nth-child(1) {
        max-width: 140px;
        width: 100%;
      }
      .content_container .chain_section > img:nth-child(2) {
        max-width: 90px;
        width: 100%;
      }
      .content_container .chain_section > img {
        width: 100%;
        max-width: 110px;
      }
      .content_container .chain_section p {
        color: #fff;
        font-family: Outfit;
        font-size: 13.733px;
        font-style: normal;
        font-weight: 600;
        letter-spacing: 0.1px;
      }
      .content_container .chain_section span {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 12.017px;
        font-style: normal;
        font-weight: 500;
        letter-spacing: 0.1px;
        margin-left: auto;
      }
      .divider {
        border-radius: 1000px;
        background: rgba(255, 255, 255, 0.1);
        mix-blend-mode: soft-light;
        width: 100%;
        height: 1px;
        margin-bottom: 12px;
      }
      .data {
        display: flex;
      }
      .data .list {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        flex: 1;
      }
      .data .list div {
        width: 100%;
        align-items: center;
        justify-content: space-between;
        display: flex;
        margin-bottom: 0.5rem;
      }
      .data .list div p {
        color: rgba(255, 255, 255, 1);
        font-family: Outfit;
        font-size: 15px;
        font-style: normal;
        font-weight: 300;
        letter-spacing: 0.1px;
        margin: 0px;
      }
      .data .list div span {
        color: rgba(255, 255, 255, 0.9);
        font-family: Outfit;
        font-size: 15px;
        font-style: normal;
        font-weight: 500;
        letter-spacing: 0.117px;
      }
      .data .list div span:nth-child(2) {
            margin-left: auto;
            color: rgba(255, 255, 255, 0.9);
            font-family: Outfit;
            font-size: 16px;
            font-style: normal;
            font-weight: 500;
            letter-spacing: 0.117px;
        }
        .data .list div span:nth-child(3) {
            color: rgba(255, 255, 255, 0.8) !important;
            text-align: right;
            font-family: Outfit;
            font-size: 14px;
            font-style: normal;
            font-weight: 400;
            letter-spacing: 0.117px;
            position: relative;
            margin-left: 0.25rem;
        }
      .address {
        color: rgba(255, 255, 255, 0.6);
        text-align: center;
        font-feature-settings: "ss06" on, "ss02" on, "liga" off;
        font-size: 12px;
        font-style: normal;
        font-weight: 400;
        letter-spacing: 0.117px;
        margin-bottom: 12px;
      }
      .loading_animation {
        animation: loading_animation 1s ease-in-out infinite alternate;
      }
      .container .footer {
        border-radius: 27.184px;
        border: 1px solid#505050;
        background: #1d1d1d;
        padding: 0.4rem 1rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 0.25rem;
      }
      .container .footer > img:nth-child(1) {
        max-width: 60px;
        width: 100%;
        object-fit: contain;
        position: relative;
        top: -2px;
      }
      .container .footer > img:nth-child(2) {
        max-width: 140px;
        width: 100%;
        object-fit: contain;
      }
      .container .overlay {
        position: absolute;
        bottom: 0;
        width: 100%;
        scale: 0.8;
      }
    </style>
  </head>
  <body>
    <section class="container card_highlighted">
      <img src= "https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/07bca5b8b10f44b99beb3fd4308c914b.png" />
      <section class="content_container">
        <section class="chain_section">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/ea6af00c71504a9bb02d6662ba740eeb.png" />
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/d73ba3b544d94bffab97339941e0558a.svg" />
        </section>
        <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/a1d73c6b450b44ec9d8a552fc33613c8.png" class="cover_image" />
        <section class="address">${userAddress}</section>
        <section class="divider"></section>
        <section class="data">
          <section class="list">
            <div>
              <p>Total Volume</p>
              <span>${volume}</span>
              <span>Top ${volumePercentile}</span>
            </div>
            <div>
              <p>Total Transactions</p>
              <span>${txncount}</span>
              <span>Top ${txncountPercentile}</span>
            </div>
            <div>
              <p>Unique Addresses</p>
              <span>${uniqueAddressesInteractedWith}</span>
              <span> Top ${uniqueAddressesInteractedWithPercentile} </span>
            </div>
            <div>
              <p>Age</p>
              <span>${age}</span>
              <span>Top ${agePercentile}</span>
            </div>
            <div>
              <p>Unique Active Days</p>
              <span>${uniqueDaysActive}</span>
              <span> Top ${uniqueDaysActivePercentile} </span>
            </div>
          </section>
        </section>
        <section class="footer">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/ccc347d2751a4dbb804ca62c1429220c.png" />
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/a83e00176f6e484da2a457d116b20fcd.png" />
        </section>
      </section>
      <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/71fc4570f40e43b086408ba527f0c5e1.png" class="overlay" />
    </section>
  </body>
</html>
"""

HTML_TEMPLATE_BASE_2 = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Outfit:100,200,300,regular,500,600,700,800%7CIBM+Plex+Sans+Hebrew:200,300,regular,500,600"
      media="all"
    />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <style>
        body {
            position: relative;
            display: flex;
            align-items: center;
            justify-content:center;
            overflow: hidden !important;
            background: transparent !important;
            margin: 0px !important
          
        }

      * {
        margin: 0px;
         overflow: hidden !important;
      }

      .container {
        position: relative;
        overflow: hidden;
        height: fit-content;
        width: 330px;
        border: 1.5px solid rgba(255, 255, 255, 0.5);
        background: linear-gradient(
          180deg,
          #252525 0%,
          #1b1b1b 25.29%,
          #131313 63.63%,
          #080808 100%
        );
      }

      .card_highlighted .divider {
        border-radius: 1000px;
        background: rgba(255, 255, 255, 0.25);
      }

      .container > img {
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
      }

      .container .content_container {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 14px;
        position: relative;
        z-index: 3;
      }

      .content_container .cover_image {
        width: 100%;
        object-position: top;
        margin-bottom: 16px;
      }

      .content_container .chain_section {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        width: 100%;
        justify-content: space-between;
        margin-bottom: 12px;
      }

      .content_container .chain_section > img:nth-child(1) {
        max-width: 100px;
        width: 100%;
      }

      .content_container .chain_section > img {
        width: 100%;
        max-width: 110px;
      }

      .content_container .chain_section p {
        color: #fff;
        font-family: Outfit;
        font-size: 13.733px;
        font-style: normal;
        font-weight: 600;
        line-height: 17.167px; /* 125% */
        letter-spacing: 0.1px;
      }

      .content_container .chain_section span {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 12.017px;
        font-style: normal;
        font-weight: 500;
        line-height: 13.733px; /* 114.286% */
        letter-spacing: 0.1px;

        margin-left: auto;
      }

      .divider {
        border-radius: 1000px;
        background: linear-gradient(
          90deg,
          rgba(255, 255, 255, 0.15) 0%,
          rgba(255, 255, 255, 0.12) 100%
        );
        width: 100%;
        height: 1px;
        margin-bottom: 16px;
      }

      .data {
        display: flex;
        gap: 1rem;
      }

      .data .list {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        flex: 1;
        margin-bottom: 0.5rem;
      }

      .data .list div {
        width: 100%;
        align-items: center;
        justify-content: space-between;
        display: flex;
        margin-bottom: 0.5rem;
      }

      .data .list div p {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        letter-spacing: 0.117px;
      }

      .card_highlighted .data .list div p {
        color: rgba(255, 255, 255, 0.9);
      }

      .data .list div span:nth-child(3) {
        color: rgba(255, 255, 255, 0.8) !important;
        text-align: right;
        font-family: Outfit;
        font-size: 14px;
        font-style: normal;
        font-weight: 400;
        letter-spacing: 0.117px;
      }

      .data .list div span:nth-child(2) {
        margin-left: auto;
        color: rgba(255, 255, 255, 0.9);
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        letter-spacing: 0.117px;
        margin-right:0.5rem;
      }

      .card_highlighted .data .list div span {
        color: #fff;
      }

      .qr_code {
        width: 90px;
        aspect-ratio: 1/1;
        padding: 4px;
        background-color: white;
      }

      .address {
        color: rgba(255, 255, 255, 0.6);
        text-align: center;
        font-feature-settings: "ss06" on, "ss02" on, "liga" off;
        font-size: 12px;
        font-style: normal;
        font-weight: 400;
        line-height: 12px; /* 109.091% */
        letter-spacing: 0.117px;
        margin-bottom: 16px;
        font-family: Outfit;
      }

      .card_highlighted .address {
        color: rgba(255, 255, 255, 0.9);
      }

      .loading_animation {
        animation: loading_animation 1s ease-in-out infinite alternate;
      }

      .container .footer {
        padding: 10px 0.75rem;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        margin-top: -0.25rem;

        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: linear-gradient(
          180deg,
          rgba(0, 0, 0, 0.16) 0%,
          rgba(0, 0, 0, 0.4) 100%
        );
        box-shadow: 0px 2px 4px 0px rgba(255, 255, 255, 0.1) inset;
      }

      .card_highlighted .footer {
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.35);
        background: linear-gradient(
          180deg,
          rgba(0, 0, 0, 0.08) 0%,
          rgba(0, 0, 0, 0.15) 100%
        );
        backdrop-filter: blur(10px);
      }

      .container .footer > img:nth-child(1) {
        width: 20px;
        height: 20px;
        flex-shrink: 0;
        object-fit: contain;
        margin-right: 0.4rem;
      }

      .container .footer > h4 {
        color: #fff;
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        line-height: 20px; /* 125% */
        letter-spacing: 0.117px;
      }

      .container .footer > p {
        color: rgba(255, 255, 255, 0.8);
        font-family: Outfit;
        font-size: 14px;
        font-style: normal;
        font-weight: 400;
        line-height: 16px; /* 114.286% */
        letter-spacing: 0.117px;
        margin-left: auto;
      }

      .container .overlay {
        position: absolute;
        bottom: 0;
      }
    </style>
  </head>

  <body>
    <section class="container card_highlighted">
      <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/07bca5b8b10f44b99beb3fd4308c914b.png" />
      <section class="content_container">
        <section class="chain_section">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/0ea3cf33cb6e401f90ccce02c1821e86.png" />
        </section>

        <img
          src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/46fda02047d6470283e2d353ffceed92.png"
          class="cover_image"
        />

        <section class="address">${userAddress}</section>

        <section class="divider"></section>

        <section class="data">
          <section class="list">
            <div>
              <p>Total Volume</p>
              <span>${volume}</span>
              <span>Top ${volumePercentile}</span>
            </div>
            <div>
              <p>Total Transactions</p>
              <span>${txncount}</span>
              <span>Top ${txncountPercentile}</span>
            </div>

            <div>
              <p>Unique Addresses</p>
              <span>${uniqueAddressesInteractedWith}</span>
              <span> Top ${uniqueAddressesInteractedWithPercentile} </span>
            </div>
            <div>
              <p>Age</p>
              <span>${age}</span>
              <span>Top ${agePercentile}</span>
            </div>
            <div>
              <p>Unique Active Days</p>
              <span>${uniqueDaysActive}</span>
              <span> Top ${uniqueDaysActivePercentile} </span>
            </div>
          </section>
        </section>

        <section class="divider"></section>

        <section class="footer">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/d51cb2faafcd42dc95de5e05358ecba8.svg" />
          <h4>Base</h4>

          <p>Base Onchain Compass Pro</p>
        </section>
      </section>
    </section>
  </body>
</html>

"""

HTML_TEMPLATE_BLAST_2 = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Outfit:100,200,300,regular,500,600,700,800%7CIBM+Plex+Sans+Hebrew:200,300,regular,500,600"
      media="all"
    />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <style>
        body {
            position: relative;
            display: flex;
            align-items: center;
            justify-content:center;
            overflow: hidden !important;
            background: transparent !important;
            margin: 0px !important
          
        }

      * {
        margin: 0px;
         overflow: hidden !important;
      }

      .container {
        position: relative;
        overflow: hidden;
        height: fit-content;
        width: 330px;
        border: 1.5px solid rgba(255, 255, 255, 0.5);
        background: linear-gradient(
          180deg,
          #252525 0%,
          #1b1b1b 25.29%,
          #131313 63.63%,
          #080808 100%
        );
      }

      .card_highlighted .divider {
        border-radius: 1000px;
        background: rgba(255, 255, 255, 0.25);
      }

      .container > img {
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
      }

      .container .content_container {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 14px;
        position: relative;
        z-index: 3;
      }

      .content_container .cover_image {
        width: 100%;
        object-position: top;
        margin-bottom: 16px;
      }

      .content_container .chain_section {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        width: 100%;
        justify-content: space-between;
        margin-bottom: 12px;
      }

      .content_container .chain_section > img:nth-child(1) {
        max-width: 100px;
        width: 100%;
      }

      .content_container .chain_section > img {
        width: 100%;
        max-width: 110px;
      }

      .content_container .chain_section p {
        color: #fff;
        font-family: Outfit;
        font-size: 13.733px;
        font-style: normal;
        font-weight: 600;
        line-height: 17.167px; /* 125% */
        letter-spacing: 0.1px;
      }

      .content_container .chain_section span {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 12.017px;
        font-style: normal;
        font-weight: 500;
        line-height: 13.733px; /* 114.286% */
        letter-spacing: 0.1px;

        margin-left: auto;
      }

      .divider {
        border-radius: 1000px;
        background: linear-gradient(
          90deg,
          rgba(255, 255, 255, 0.15) 0%,
          rgba(255, 255, 255, 0.12) 100%
        );
        width: 100%;
        height: 1px;
        margin-bottom: 16px;
      }

      .data {
        display: flex;
        gap: 1rem;
      }

      .data .list {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        flex: 1;
        margin-bottom: 0.5rem;
      }

      .data .list div {
        width: 100%;
        align-items: center;
        justify-content: space-between;
        display: flex;
        margin-bottom: 0.5rem;
      }

      .data .list div p {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        letter-spacing: 0.117px;
      }

      .card_highlighted .data .list div p {
        color: rgba(255, 255, 255, 0.9);
      }

      .data .list div span:nth-child(2) {
        margin-left: auto;
        color: rgba(255, 255, 255, 0.9);
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        letter-spacing: 0.117px;
        margin-right:0.5rem;
      }

      .card_highlighted .data .list div span {
        color: #fff;
      }

      .qr_code {
        width: 90px;
        aspect-ratio: 1/1;
        padding: 4px;
        background-color: white;
      }

      .address {
        color: rgba(255, 255, 255, 0.6);
        text-align: center;
        font-feature-settings: "ss06" on, "ss02" on, "liga" off;
        font-size: 12px;
        font-style: normal;
        font-weight: 400;
        line-height: 12px; /* 109.091% */
        letter-spacing: 0.117px;
        margin-bottom: 16px;
        font-family: Outfit;
      }

      .card_highlighted .address {
        color: rgba(255, 255, 255, 0.9);
      }

      .loading_animation {
        animation: loading_animation 1s ease-in-out infinite alternate;
      }

      .container .footer {
        padding: 10px 0.75rem;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        margin-top: -0.25rem;

        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: linear-gradient(
          180deg,
          rgba(0, 0, 0, 0.16) 0%,
          rgba(0, 0, 0, 0.4) 100%
        );
        box-shadow: 0px 2px 4px 0px rgba(255, 255, 255, 0.1) inset;
      }

      .card_highlighted .footer {
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.35);
        background: linear-gradient(
          180deg,
          rgba(0, 0, 0, 0.08) 0%,
          rgba(0, 0, 0, 0.15) 100%
        );
        backdrop-filter: blur(10px);
      }

      .container .footer > img:nth-child(1) {
        width: 80px;
        height: 16px;
        flex-shrink: 0;
        object-fit: contain;
        margin-right: 0.4rem;
      }

      .container .footer > h4 {
        color: #fff;
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        line-height: 20px; /* 125% */
        letter-spacing: 0.117px;
      }

      .container .footer > p {
        color: rgba(255, 255, 255, 0.8);
        font-family: Outfit;
        font-size: 14px;
        font-style: normal;
        font-weight: 400;
        line-height: 16px; /* 114.286% */
        letter-spacing: 0.117px;
        margin-left: auto;
      }

      .container .overlay {
        position: absolute;
        bottom: 0;
      }
    </style>
  </head>

  <body>
    <section class="container card_highlighted">
      <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/07bca5b8b10f44b99beb3fd4308c914b.png" />
      <section class="content_container">
        <section class="chain_section">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/0ea3cf33cb6e401f90ccce02c1821e86.png" />
        </section>

        <img
          src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/de0b53a0e2654961a81e2cf5a8ffb0f6.png"
          class="cover_image"
        />

        <section class="address">${userAddress}</section>

        <section class="divider"></section>

        <section class="data">
          <section class="list">
            <div>
              <p>Total Volume</p>
              <span>${volume}</span>
            </div>
            <div>
              <p>Total Transactions</p>
              <span>${txncount}</span>
            </div>

            <div>
              <p>Unique Addresses</p>
              <span>${uniqueAddressesInteractedWith}</span>
            </div>
            <div>
              <p>Age</p>
              <span>${age}</span>
            </div>
            <div>
              <p>Unique Active Days</p>
              <span>${uniqueDaysActive}</span>
            </div>
          </section>
        </section>

        <section class="divider"></section>

        <section class="footer">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/68cf5d453a5249d6b7f6c5c9a78267e4.png" />

          <p>BLAST Onchain Compass</p>
        </section>
      </section>
    </section>
  </body>
</html>

"""

HTML_TEMPLATE_ZKSYNC_2 = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Outfit:100,200,300,regular,500,600,700,800%7CIBM+Plex+Sans+Hebrew:200,300,regular,500,600"
      media="all"
    />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <style>
        body {
            position: relative;
            display: flex;
            align-items: center;
            justify-content:center;
            overflow: hidden !important;
            background: transparent !important;
            margin: 0px !important
          
        }

      * {
        margin: 0px;
         overflow: hidden !important;
      }

      .container {
        position: relative;
        overflow: hidden;
        height: fit-content;
        width: 330px;
        border: 1.5px solid rgba(255, 255, 255, 0.5);
        background: linear-gradient(
          180deg,
          #252525 0%,
          #1b1b1b 25.29%,
          #131313 63.63%,
          #080808 100%
        );
      }

      .card_highlighted .divider {
        border-radius: 1000px;
        background: rgba(255, 255, 255, 0.25);
      }

      .container > img {
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
      }

      .container .content_container {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 14px;
        position: relative;
        z-index: 3;
      }

      .content_container .cover_image {
        width: 100%;
        object-position: top;
        margin-bottom: 16px;
      }

      .content_container .chain_section {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        width: 100%;
        justify-content: space-between;
        margin-bottom: 12px;
      }

      .content_container .chain_section > img:nth-child(1) {
        max-width: 100px;
        width: 100%;
      }

      .content_container .chain_section > img {
        width: 100%;
        max-width: 110px;
      }

      .content_container .chain_section p {
        color: #fff;
        font-family: Outfit;
        font-size: 13.733px;
        font-style: normal;
        font-weight: 600;
        line-height: 17.167px; /* 125% */
        letter-spacing: 0.1px;
      }

      .content_container .chain_section span {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 12.017px;
        font-style: normal;
        font-weight: 500;
        line-height: 13.733px; /* 114.286% */
        letter-spacing: 0.1px;

        margin-left: auto;
      }

      .divider {
        border-radius: 1000px;
        background: linear-gradient(
          90deg,
          rgba(255, 255, 255, 0.15) 0%,
          rgba(255, 255, 255, 0.12) 100%
        );
        width: 100%;
        height: 1px;
        margin-bottom: 16px;
      }

      .data {
        display: flex;
        gap: 1rem;
      }

      .data .list {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        flex: 1;
        margin-bottom: 0.5rem;
      }

      .data .list div {
        width: 100%;
        align-items: center;
        justify-content: space-between;
        display: flex;
        margin-bottom: 0.5rem;
      }

      .data .list div p {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        letter-spacing: 0.117px;
      }

      .card_highlighted .data .list div p {
        color: rgba(255, 255, 255, 0.9);
      }

      .data .list div span:nth-child(2) {
        margin-left: auto;
        color: rgba(255, 255, 255, 0.9);
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        letter-spacing: 0.117px;
        margin-right:0.5rem;
      }

      .card_highlighted .data .list div span {
        color: #fff;
      }

      .qr_code {
        width: 90px;
        aspect-ratio: 1/1;
        padding: 4px;
        background-color: white;
      }

      .address {
        color: rgba(255, 255, 255, 0.6);
        text-align: center;
        font-feature-settings: "ss06" on, "ss02" on, "liga" off;
        font-size: 12px;
        font-style: normal;
        font-weight: 400;
        line-height: 12px; /* 109.091% */
        letter-spacing: 0.117px;
        margin-bottom: 16px;
        font-family: Outfit;
      }

      .card_highlighted .address {
        color: rgba(255, 255, 255, 0.9);
      }

      .loading_animation {
        animation: loading_animation 1s ease-in-out infinite alternate;
      }

      .container .footer {
        padding: 10px 0.75rem;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        margin-top: -0.25rem;

        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: linear-gradient(
          180deg,
          rgba(0, 0, 0, 0.16) 0%,
          rgba(0, 0, 0, 0.4) 100%
        );
        box-shadow: 0px 2px 4px 0px rgba(255, 255, 255, 0.1) inset;
      }

      .card_highlighted .footer {
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.35);
        background: linear-gradient(
          180deg,
          rgba(0, 0, 0, 0.08) 0%,
          rgba(0, 0, 0, 0.15) 100%
        );
        backdrop-filter: blur(10px);
      }

      .container .footer > img:nth-child(1) {
        width: 82px;
        height: 16px;
        flex-shrink: 0;
        object-fit: contain;
        margin-right: 0.4rem;
      }

      .container .footer > h4 {
        color: #fff;
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        line-height: 20px; /* 125% */
        letter-spacing: 0.117px;
      }

      .container .footer > p {
        color: rgba(255, 255, 255, 0.8);
        font-family: Outfit;
        font-size: 14px;
        font-style: normal;
        font-weight: 400;
        line-height: 16px; /* 114.286% */
        letter-spacing: 0.117px;
        margin-left: auto;
      }

      .container .overlay {
        position: absolute;
        bottom: 0;
      }
    </style>
  </head>

  <body>
    <section class="container card_highlighted">
      <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/07bca5b8b10f44b99beb3fd4308c914b.png" />
      <section class="content_container">
        <section class="chain_section">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/0ea3cf33cb6e401f90ccce02c1821e86.png" />
        </section>

        <img
          src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/f0a1cc4e4f2a470bbb5466a900a016a1.png"
          class="cover_image"
        />

        <section class="address">${userAddress}</section>

        <section class="divider"></section>

        <section class="data">
          <section class="list">
            <div>
              <p>Total Volume</p>
              <span>${volume}</span>
            </div>
            <div>
              <p>Total Transactions</p>
              <span>${txncount}</span>
            </div>

            <div>
              <p>Unique Addresses</p>
              <span>${uniqueAddressesInteractedWith}</span>
            </div>
            <div>
              <p>Age</p>
              <span>${age}</span>
            </div>
            <div>
              <p>Unique Active Days</p>
              <span>${uniqueDaysActive}</span>
            </div>
          </section>
        </section>

        <section class="divider"></section>

        <section class="footer">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/674f2e70ecb74d67885e56ffe1afc40a.png" />

          <p>zkSync Onchain Compass</p>
        </section>
      </section>
    </section>
  </body>
</html>

"""

HTML_TEMPLATE_MODE_2 = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Outfit:100,200,300,regular,500,600,700,800%7CIBM+Plex+Sans+Hebrew:200,300,regular,500,600"
      media="all"
    />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <style>
        body {
            position: relative;
            display: flex;
            align-items: center;
            justify-content:center;
            overflow: hidden !important;
            background: transparent !important;
            margin: 0px !important
          
        }

      * {
        margin: 0px;
         overflow: hidden !important;
      }

      .container {
        position: relative;
        overflow: hidden;
        height: fit-content;
        width: 330px;
        border: 1.5px solid rgba(255, 255, 255, 0.5);
        background: linear-gradient(
          180deg,
          #252525 0%,
          #1b1b1b 25.29%,
          #131313 63.63%,
          #080808 100%
        );
      }

      .card_highlighted .divider {
        border-radius: 1000px;
        background: rgba(255, 255, 255, 0.25);
      }

      .container > img {
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
      }

      .container .content_container {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 14px;
        position: relative;
        z-index: 3;
      }

      .content_container .cover_image {
        width: 100%;
        object-position: top;
        margin-bottom: 16px;
      }

      .content_container .chain_section {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        width: 100%;
        justify-content: space-between;
        margin-bottom: 12px;
      }

      .content_container .chain_section > img:nth-child(1) {
        max-width: 100px;
        width: 100%;
      }

      .content_container .chain_section > img {
        width: 100%;
        max-width: 110px;
      }

      .content_container .chain_section p {
        color: #fff;
        font-family: Outfit;
        font-size: 13.733px;
        font-style: normal;
        font-weight: 600;
        line-height: 17.167px; /* 125% */
        letter-spacing: 0.1px;
      }

      .content_container .chain_section span {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 12.017px;
        font-style: normal;
        font-weight: 500;
        line-height: 13.733px; /* 114.286% */
        letter-spacing: 0.1px;

        margin-left: auto;
      }

      .divider {
        border-radius: 1000px;
        background: linear-gradient(
          90deg,
          rgba(255, 255, 255, 0.15) 0%,
          rgba(255, 255, 255, 0.12) 100%
        );
        width: 100%;
        height: 1px;
        margin-bottom: 16px;
      }

      .data {
        display: flex;
        gap: 1rem;
      }

      .data .list {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        flex: 1;
        margin-bottom: 0.5rem;
      }

      .data .list div {
        width: 100%;
        align-items: center;
        justify-content: space-between;
        display: flex;
        margin-bottom: 0.5rem;
      }

      .data .list div p {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        letter-spacing: 0.117px;
      }

      .card_highlighted .data .list div p {
        color: rgba(255, 255, 255, 0.9);
      }

      .data .list div span:nth-child(2) {
        margin-left: auto;
        color: rgba(255, 255, 255, 0.9);
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        letter-spacing: 0.117px;
        margin-right:0.5rem;
      }

      .card_highlighted .data .list div span {
        color: #fff;
      }

      .qr_code {
        width: 90px;
        aspect-ratio: 1/1;
        padding: 4px;
        background-color: white;
      }

      .address {
        color: rgba(255, 255, 255, 0.6);
        text-align: center;
        font-feature-settings: "ss06" on, "ss02" on, "liga" off;
        font-size: 12px;
        font-style: normal;
        font-weight: 400;
        line-height: 12px; /* 109.091% */
        letter-spacing: 0.117px;
        margin-bottom: 16px;
        font-family: Outfit;
      }

      .card_highlighted .address {
        color: rgba(255, 255, 255, 0.9);
      }

      .loading_animation {
        animation: loading_animation 1s ease-in-out infinite alternate;
      }

      .container .footer {
        padding: 10px 4px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        margin-top: -0.25rem;

        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: linear-gradient(
          180deg,
          rgba(0, 0, 0, 0.16) 0%,
          rgba(0, 0, 0, 0.4) 100%
        );
        box-shadow: 0px 2px 4px 0px rgba(255, 255, 255, 0.1) inset;
      }

      .card_highlighted .footer {
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.35);
        background: linear-gradient(
          180deg,
          rgba(0, 0, 0, 0.08) 0%,
          rgba(0, 0, 0, 0.15) 100%
        );
        backdrop-filter: blur(10px);
      }

      .container .footer > img:nth-child(1) {
        width: 80px;
        height: 16px;
        flex-shrink: 0;
        object-fit: contain;
        margin-right: 0.4rem;
      }

      .container .footer > h4 {
        color: #fff;
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        line-height: 20px; /* 125% */
        letter-spacing: 0.117px;
      }

      .container .footer > p {
        color: rgba(255, 255, 255, 0.8);
        font-family: Outfit;
        font-size: 14px;
        font-style: normal;
        font-weight: 400;
        line-height: 16px; /* 114.286% */
        letter-spacing: 0.117px;
        margin-left: auto;
      }

      .container .overlay {
        position: absolute;
        bottom: 0;
      }
    </style>
  </head>

  <body>
    <section class="container card_highlighted">
      <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/07bca5b8b10f44b99beb3fd4308c914b.png" />
      <section class="content_container">
        <section class="chain_section">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/0ea3cf33cb6e401f90ccce02c1821e86.png" />
        </section>

        <img
          src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/e9e66a6151f146d89f7e411a94110db3.png"
          class="cover_image"
        />

        <section class="address">${userAddress}</section>

        <section class="divider"></section>

        <section class="data">
          <section class="list">
            <div>
              <p>Total Volume</p>
              <span>${volume}</span>
            </div>
            <div>
              <p>Total Transactions</p>
              <span>${txncount}</span>
            </div>

            <div>
              <p>Unique Addresses</p>
              <span>${uniqueAddressesInteractedWith}</span>
            </div>
            <div>
              <p>Age</p>
              <span>${age}</span>
            </div>
            <div>
              <p>Unique Active Days</p>
              <span>${uniqueDaysActive}</span>
            </div>
          </section>
        </section>

        <section class="divider"></section>

        <section class="footer">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/55da8fdba6854ba2b2a10f986036620f.png" />

          <p>MODE Onchain Compass</p>
        </section>
      </section>
    </section>
  </body>
</html>

"""

HTML_TEMPLATE_ZORA_2 = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Outfit:100,200,300,regular,500,600,700,800%7CIBM+Plex+Sans+Hebrew:200,300,regular,500,600"
      media="all"
    />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <style>
        body {
            position: relative;
            display: flex;
            align-items: center;
            justify-content:center;
            overflow: hidden !important;
            background: transparent !important;
            margin: 0px !important
          
        }

      * {
        margin: 0px;
         overflow: hidden !important;
      }

      .container {
        position: relative;
        overflow: hidden;
        height: fit-content;
        width: 330px;
        border: 1.5px solid rgba(255, 255, 255, 0.5);
        background: linear-gradient(
          180deg,
          #252525 0%,
          #1b1b1b 25.29%,
          #131313 63.63%,
          #080808 100%
        );
      }

      .card_highlighted .divider {
        border-radius: 1000px;
        background: rgba(255, 255, 255, 0.25);
      }

      .container > img {
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
      }

      .container .content_container {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 14px;
        position: relative;
        z-index: 3;
      }

      .content_container .cover_image {
        width: 100%;
        object-position: top;
        margin-bottom: 16px;
      }

      .content_container .chain_section {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        width: 100%;
        justify-content: space-between;
        margin-bottom: 12px;
      }

      .content_container .chain_section > img:nth-child(1) {
        max-width: 100px;
        width: 100%;
      }

      .content_container .chain_section > img {
        width: 100%;
        max-width: 110px;
      }

      .content_container .chain_section p {
        color: #fff;
        font-family: Outfit;
        font-size: 13.733px;
        font-style: normal;
        font-weight: 600;
        line-height: 17.167px; /* 125% */
        letter-spacing: 0.1px;
      }

      .content_container .chain_section span {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 12.017px;
        font-style: normal;
        font-weight: 500;
        line-height: 13.733px; /* 114.286% */
        letter-spacing: 0.1px;

        margin-left: auto;
      }

      .divider {
        border-radius: 1000px;
        background: linear-gradient(
          90deg,
          rgba(255, 255, 255, 0.15) 0%,
          rgba(255, 255, 255, 0.12) 100%
        );
        width: 100%;
        height: 1px;
        margin-bottom: 16px;
      }

      .data {
        display: flex;
        gap: 1rem;
      }

      .data .list {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        flex: 1;
        margin-bottom: 0.5rem;
      }

      .data .list div {
        width: 100%;
        align-items: center;
        justify-content: space-between;
        display: flex;
        margin-bottom: 0.5rem;
      }

      .data .list div p {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        letter-spacing: 0.117px;
      }

      .card_highlighted .data .list div p {
        color: rgba(255, 255, 255, 0.9);
      }

      .data .list div span:nth-child(2) {
        margin-left: auto;
        color: rgba(255, 255, 255, 0.9);
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        letter-spacing: 0.117px;
        margin-right:0.5rem;
      }

      .card_highlighted .data .list div span {
        color: #fff;
      }

      .qr_code {
        width: 90px;
        aspect-ratio: 1/1;
        padding: 4px;
        background-color: white;
      }

      .address {
        color: rgba(255, 255, 255, 0.6);
        text-align: center;
        font-feature-settings: "ss06" on, "ss02" on, "liga" off;
        font-size: 12px;
        font-style: normal;
        font-weight: 400;
        line-height: 12px; /* 109.091% */
        letter-spacing: 0.117px;
        margin-bottom: 16px;
        font-family: Outfit;
      }

      .card_highlighted .address {
        color: rgba(255, 255, 255, 0.9);
      }

      .loading_animation {
        animation: loading_animation 1s ease-in-out infinite alternate;
      }

      .container .footer {
        padding: 10px 4px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        margin-top: -0.25rem;

        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: linear-gradient(
          180deg,
          rgba(0, 0, 0, 0.16) 0%,
          rgba(0, 0, 0, 0.4) 100%
        );
        box-shadow: 0px 2px 4px 0px rgba(255, 255, 255, 0.1) inset;
      }

      .card_highlighted .footer {
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.35);
        background: linear-gradient(
          180deg,
          rgba(0, 0, 0, 0.08) 0%,
          rgba(0, 0, 0, 0.15) 100%
        );
        backdrop-filter: blur(10px);
      }

      .container .footer > img:nth-child(1) {
        width: 80px;
        height: 16px;
        flex-shrink: 0;
        object-fit: contain;
        margin-right: 0.4rem;
      }

      .container .footer > h4 {
        color: #fff;
        font-family: Outfit;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        line-height: 20px; /* 125% */
        letter-spacing: 0.117px;
      }

      .container .footer > p {
        color: rgba(255, 255, 255, 0.8);
        font-family: Outfit;
        font-size: 14px;
        font-style: normal;
        font-weight: 400;
        line-height: 16px; /* 114.286% */
        letter-spacing: 0.117px;
        margin-left: auto;
      }

      .container .overlay {
        position: absolute;
        bottom: 0;
      }
    </style>
  </head>

  <body>
    <section class="container card_highlighted">
      <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/07bca5b8b10f44b99beb3fd4308c914b.png" />
      <section class="content_container">
        <section class="chain_section">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/0ea3cf33cb6e401f90ccce02c1821e86.png" />
        </section>

        <img
          src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/8ae74242d96d4f29aad26bcaa310e881.png"
          class="cover_image"
        />

        <section class="address">${userAddress}</section>

        <section class="divider"></section>

        <section class="data">
          <section class="list">
            <div>
              <p>Total Volume</p>
              <span>${volume}</span>
            </div>
            <div>
              <p>Total Transactions</p>
              <span>${txncount}</span>
            </div>

            <div>
              <p>Unique Addresses</p>
              <span>${uniqueAddressesInteractedWith}</span>
            </div>
            <div>
              <p>Age</p>
              <span>${age}</span>
            </div>
            <div>
              <p>Unique Active Days</p>
              <span>${uniqueDaysActive}</span>
            </div>
          </section>
        </section>

        <section class="divider"></section>

        <section class="footer">
          <img src="https://static.highongrowth.xyz/enterprise/6436a5f81cda49dc8a18a8f3/a94ec4cf9f304496a32594c6fe0e576d.png" />

          <p>ZORA Onchain Compass</p>
        </section>
      </section>
    </section>
  </body>
</html>

"""