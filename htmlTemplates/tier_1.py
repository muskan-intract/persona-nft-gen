HTML_TEMPLATE_ZKEVM_1 = """
<!DOCTYPE html>
<html lang="english">
  <head>
    <title>exported project</title>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&amp;display=swap"
      data-tag="font"
    />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Outfit:wght@100;200;300;400;500;600;700;800;900&amp;display=swap"
      data-tag="font"
    />

    <style data-tag="reset-style-sheet">
      html {
        line-height: 1.15;
      }
      body {
        margin: 0;
        background-color: black;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100svh;
      }
      * {
        box-sizing: border-box;
        border-width: 0;
        border-style: solid;
      }
      p,
      li,
      ul,
      pre,
      div,
      h1,
      h2,
      h3,
      h4,
      h5,
      h6,
      figure,
      blockquote,
      figcaption {
        margin: 0;
        padding: 0;
      }
      button {
        background-color: transparent;
      }
      button,
      input,
      optgroup,
      select,
      textarea {
        font-family: inherit;
        font-size: 100%;
        line-height: 1.15;
        margin: 0;
      }
      button,
      select {
        text-transform: none;
      }
      button,
      [type="button"],
      [type="reset"],
      [type="submit"] {
        -webkit-appearance: button;
      }
      button::-moz-focus-inner,
      [type="button"]::-moz-focus-inner,
      [type="reset"]::-moz-focus-inner,
      [type="submit"]::-moz-focus-inner {
        border-style: none;
        padding: 0;
      }
      button:-moz-focus,
      [type="button"]:-moz-focus,
      [type="reset"]:-moz-focus,
      [type="submit"]:-moz-focus {
        outline: 1px dotted ButtonText;
      }
      a {
        color: inherit;
        text-decoration: inherit;
      }
      input {
        padding: 2px 4px;
      }
      img {
        display: block;
      }
      html {
        scroll-behavior: smooth;
      }
    </style>

    <style data-tag="index.css">
      .container {
        position: relative;
        overflow: hidden;
        height: fit-content;
        border-radius: 24px;
        width: 360px;
        border: 1px rgba(255, 255, 255, 0.3) solid;
      }

      .container .loader_container {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;

        display: flex;
        align-items: center;
        justify-content: center;
        backdrop-filter: blur(4px);
        background-color: rgba(0, 0, 0, 0.2);
        z-index: 2;
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

      .container .metal_border {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        object-fit: cover;
      }

      .container .content_container {
	width: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	padding: 1rem;
	position: relative;
}
     

      .content_container .cover_image {
	aspect-ratio: 4/3.6;
	width: 100%;
	object-fit: contain;
	object-position: top;
	border-radius: 12px;
}

      .content_container .chain_section {
        display: flex;
        align-items: center;
  margin-top: 12.8px;
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
          #fff 0%,
          rgba(255, 255, 255, 0.8) 100%
        );
        mix-blend-mode: soft-light;
        width: 100%;
        height: 1px;
        margin: 12.8px 0px;
      }

      .data {
        display: flex;
      }

      .data .list {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        flex: 1;
        min-width: 0;
        margin-right: 12.8px;
      }

      .data .list div {
        width: 100%;
        align-items: center;
        justify-content: space-between;
        display: flex;
      }

      .data .list div p {
        color: rgba(255, 255, 255, 0.6);
        font-family: Outfit;
        font-size: 13.017px;
        font-style: normal;
        font-weight: 400;
        line-height: 13.733px; /* 114.286% */
        letter-spacing: 0.1px;
      }

      .data .list div span {
        color: rgba(255, 255, 255, 0.9);
        font-family: Outfit;
        font-size: 14px;
        font-style: normal;
        font-weight: 600;
        line-height: 16px; /* 114.286% */
        letter-spacing: 0.117px;
        word-break: break-all;
      }

      .content_container .chain_section > img {
	width: 30px;
  margin-right: 8px;
}

      .qr_code {
        width: 112px;
        aspect-ratio: 1/1;
        padding: 4px;
        background-color: white;
        flex-shrink: 0;
      }

      .qr_code img {
        width: 100%;
        height: 100%;
        object-fit: contain;
      }

      .address {
        color: rgba(255, 255, 255, 0.6);
        text-align: center;
        font-family: Outfit;
        font-size: 12px;
        font-style: normal;
        font-weight: 500;
        line-height: 12px; /* 100% */
        letter-spacing: 0.117px;
      }
    </style>
  </head>
  <body>
    <section class="container">
      <img class="bg_image" src="file:///var/task/assets/nft-card-bg.png" />

      <section class="content_container">
        <img src="file:///var/task/assets/nft-cover-image.png" class="cover_image" />

        <section class="chain_section">
          <img src="file:///var/task/assets/zkevm.png" />
        

          <p>zkEVM Chain</p>

					<span>// ONCHAIN REPUTATION</span>
        </section>

        <section class="divider"></section>

        <section class="data">
          <section class="list">
            <div>
              <p>Total Transactions</p>
              <span>${txncount}</span>
            </div>
            <div>
              <p>Total Gas Spent</p>
              <span>${gasPaid}</span>
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

          <section class="qr_code">
            <img src="file:///var/task/assets/qr_code.png" />
          </section>
        </section>

        <section class="divider"></section>

        <section class="address">${userAddress}</section>
      </section>
    </section>
  </body>
</html>
"""

HTML_TEMPLATE_LINEA_1 = """
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
        
        * {
          overflow: hidden !important;
        }
        
        body {
            position: relative;
            display: flex;
            align-items: center;
            justify-content:center;
            overflow: hidden !important;
            background: transparent !important;
            margin: 0px !important
          
        }
			.container {
				font-family: "Outfit";
				position: relative;
				overflow: hidden;
				height: fit-content;
				width: 330px;
				background-color: #121212;
				border: 1px solid #505050;
        overflow: hidden !important;
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
				background: rgba(255, 255, 255, 0.1);
				mix-blend-mode: soft-light;
				width: 100%;
				height: 1px;
				margin-bottom: 12px;
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
			}

			.data .list div {
				width: 100%;
				align-items: center;
				justify-content: space-between;
				display: flex;
			  margin-bottom: 0.55rem;
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

			.address {
				color: rgba(255, 255, 255, 0.6);
				text-align: center;
				font-feature-settings: "ss06" on, "ss02" on, "liga" off;
				font-size: 12px;
				font-style: normal;
				font-weight: 400;
				line-height: 12px; /* 109.091% */
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
		<section class="container">
			<section class="content_container">
				<section class="chain_section">
					<img src="file:///var/task/assets/linea/defi-voyager.png" />

					<img src="file:///var/task/assets/linea/intract-logo.png" />
				</section>

				<img
					src="file:///var/task/assets/linea/cover.png"
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

				<section class="footer">
					<img src="file:///var/task/assets/linea/linea-logo.png" />
					<img
						src="file:///var/task/assets/linea/linea-voyage-deFi.png"
					/>
				</section>
			</section>

			<img
				src="file:///var/task/assets/linea/blocks.png"
				class="overlay"
			/>
		</section>
	</body>
</html>
"""

HTML_TEMPLATE_BASE_1 = """
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
        border: 1.5px solid rgba(255, 255, 255, 0.2);
        background: linear-gradient(
          180deg,
          #252525 0%,
          #1b1b1b 25.29%,
          #131313 63.63%,
          #080808 100%
        );
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
        font-family: Outfit;
        margin-bottom: 16px;
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
        gap: 0.4rem;

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
    <section class="container">
      <section class="content_container">
        <section class="chain_section">
          <img src="./base/intract-logo.png" />
        </section>

        <img src="./base/nft-samurai.png" class="cover_image" />

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
          <img src="./base/base-logo.svg" />
          <h4>Base</h4>

          <p>Base Onchain Compass Pro</p>
        </section>
      </section>
    </section>
  </body>
</html>
"""