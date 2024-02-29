function calculateDiscount(price, isPremiumCustomer, isWeekend) {
  const discount = isPremiumCustomer ? (isWeekend ? 0.1 : 0.05) : (isWeekend ? 0.05 : 0);
  const discountedPrice = price - (price * discount);
  return discountedPrice;
}

