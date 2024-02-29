class OrderManager {
  constructor() {
    this.items = [];
    this.status = 'pending';
  }

  addItem(item) {
    this.items.push(item);
  }

  removeItem(item) {
    const index = this.items.indexOf(item);
    if (index !== -1) {
      this.items.splice(index, 1);
    }
  }

  calculateTotal() {
    let total = 0;
    for (const item of this.items) {
      total += item.price;
    }
    return total;
  }

  applyDiscount(discountPercentage) {
    const total = this.calculateTotal();
    const discountAmount = (total * discountPercentage) / 100;
    return total - discountAmount;
  }

  setStatusBasedOnRules() {
    if (this.items.length === 0) {
      this.status = 'empty';
    } else if (this.items.length === 1) {
      this.status = 'in progress';
    } else {
      this.status = 'completed';
    }
  }
}

module.exports = OrderManager;
