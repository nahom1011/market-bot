let currentLang = 'en';

const products = [
  { id: "m_shoe1", gender: "male", category: "shoes", name_en: "Men's Running Shoes", name_am: "የወንድ ሩጫ ጫማ", image: "https://via.placeholder.com/300x200?text=Mens+Shoes+1" },
  { id: "m_shoe2", gender: "male", category: "shoes", name_en: "Leather Shoes", name_am: "የቆዳ ጫማ", image: "https://via.placeholder.com/300x200?text=Mens+Shoes+2" },
  { id: "m_perfume1", gender: "male", category: "perfumes", name_en: "Classic Cologne", name_am: "ክላሲክ ኮሎን", image: "https://via.placeholder.com/300x200?text=Mens+Perfume" },
  { id: "f_wig1", gender: "female", category: "wigs", name_en: "Long Curly Wig", name_am: "ረዥም ዊግ", image: "https://via.placeholder.com/300x200?text=Wig" }
];

// Translation function
function t(key) {
  const langObj = window["lang_" + currentLang] || window.lang_en;
  return langObj[key] || key;
}

function renderProducts(categoryFilter = "all", searchTerm = "") {
  const container = document.getElementById("products");
  container.innerHTML = "";

  let filtered = products;

  if (categoryFilter !== "all") {
    filtered = filtered.filter(p => p.category === categoryFilter);
  }

  if (searchTerm) {
    filtered = filtered.filter(p => {
      const name = currentLang === 'am' ? p.name_am : p.name_en;
      return name.toLowerCase().includes(searchTerm.toLowerCase());
    });
  }

  if (filtered.length === 0) {
    container.innerHTML = `<p class="text-gray-500 italic">${t("no_products_found") || "No products found."}</p>`;
    return;
  }

  filtered.forEach(p => {
    const name = currentLang === 'am' ? p.name_am : p.name_en;
    const card = document.createElement("div");
    card.className = "bg-white rounded-2xl shadow-lg overflow-hidden transform transition duration-300 hover:scale-105 hover:shadow-xl animate-fade-in";
    card.innerHTML = `
      <img src="${p.image}" alt="${name}" class="w-full h-48 object-cover" />
      <div class="p-4">
        <h4 class="text-lg font-bold text-gray-800 mb-2">${name}</h4>
        <button class="mr-2 bg-green-500 hover:bg-green-600 text-white px-3 py-1 rounded shadow-sm" onclick="contact('${p.id}')">${t("contact")}</button>
        <button class="bg-yellow-400 hover:bg-yellow-500 text-white px-3 py-1 rounded shadow-sm" onclick="rate('${p.id}')">${t("rate")}</button>
      </div>
    `;
    container.appendChild(card);
  });
}

function contact(productId) {
  alert(`${t("contact")} requested for product: ${productId}`);
}

function rate(productId) {
  let rating = prompt(t("rate_prompt") || "Rate this product (1-5):");
  rating = parseInt(rating);
  if (isNaN(rating) || rating < 1 || rating > 5) {
    alert(t("invalid_rating") || "Invalid rating.");
    return;
  }
  alert(t("rating_thanks"));
}

function updateTexts() {
  const langObj = window["lang_" + currentLang] || window.lang_en;

  document.getElementById("searchInput").placeholder = langObj["search_placeholder"] || "Search products...";
  
  // Update category options text dynamically
  const categorySelect = document.getElementById("categoryFilter");
  categorySelect.options[0].text = langObj["categories"] || "Categories";
  categorySelect.options[1].text = langObj["shoes"] || "Shoes";
  categorySelect.options[2].text = langObj["perfumes"] || "Perfumes";
  categorySelect.options[3].text = langObj["cosmetics"] || "Cosmetics";
  categorySelect.options[4].text = langObj["wigs"] || "Wigs";

  // Update header title & subtitle
  document.getElementById("header-title").textContent = langObj["store_title"] || "Welcome to Mini Store";
  document.getElementById("header-subtitle").textContent = langObj["store_subtitle"] || "Browse & shop the best products. Earn 5 birr per referral.";
}

// Event Listeners
document.getElementById("categoryFilter").addEventListener("change", e => {
  renderProducts(e.target.value, document.getElementById("searchInput").value);
});

document.getElementById("searchInput").addEventListener("input", e => {
  renderProducts(document.getElementById("categoryFilter").value, e.target.value);
});

document.getElementById("langSelect").addEventListener("change", e => {
  currentLang = e.target.value;
  updateTexts();
  renderProducts(document.getElementById("categoryFilter").value, document.getElementById("searchInput").value);
});

// Initial
updateTexts();
renderProducts();
